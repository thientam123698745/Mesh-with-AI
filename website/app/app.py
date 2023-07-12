import base64
import json
import requests
import time
from flask import Flask, render_template, request
from flask_mqtt import Mqtt
app = Flask(__name__, template_folder='templates')

# Cấu hình kết nối tới broker
app.config['MQTT_BROKER_URL'] = 'mqtt3.thingspeak.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config["MQTT_TRANSPORT"] = "TCP"
app.config['MQTT_USERNAME'] = 'IgAhECIoJjcSHhwwCR49DTs'
app.config['MQTT_CLIENT_ID'] = 'IgAhECIoJjcSHhwwCR49DTs'
app.config['MQTT_PASSWORD'] = 'omKdOVvpxyI2Cmh4wDOYNe4R'
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_CLEAN_SESSION'] = True
app.config['MQTT_REFRESH_TIME'] = 5.0 # refresh time in seconds
# Khởi tạo đối tượng MQTT
mqtt = Mqtt(app, connect_async=True)
mqtt.init_app(app)
topic6 = "channels/2173391/publish/fields/field6"
topic1 = "channels/2173391/publish/fields/field1"
topic2 = "channels/2173391/publish/fields/field2"
image_urls = []
API_KEY = 'PofhJGrHUoTJ9gL5dPQ5vgenbk8KWfHtSr4EVYsAbxI9STXYd2'



def encode_file(url):
    response = requests.get(url)
    content = response.content
    encoded_content = base64.b64encode(content).decode("ascii")
    return encoded_content

def identify_plant(file_names):
    response = requests.post(
        "https://api.plant.id/v2/health_assessment",
        json={
            "images": [encode_file(img) for img in file_names],
            "modifiers": ["crops_fast" ,"similar_images"],
            "language": "en",
            "disease_details": ["cause",
                            "common_names",
                            "classification",
                            "description",
                            "treatment",
                            "url",
                            ],
        },
        headers={
            "Content-Type": "application/json",
            "Api-Key": API_KEY,
        })
    return response.json()

def process_text(text):
    text['health_assessment']['is_healthy']
    text['health_assessment']['is_healthy_probability']
    array = text['health_assessment']['diseases']
    for name_index in array:
        name_index['name']

    for name_index in array:
        name_index['probability']

    for name_index in array:
        name_index['disease_details']['url']

    for name_index in array:
        name_index['disease_details']['description']
    

def get_data(field ,number_of_data=10):
    # URL của endpoint hoặc API
    url = f'https://api.thingspeak.com/channels/2173391/fields/{field}.json?results={number_of_data}'

    # Thực hiện yêu cầu GET để lấy dữ liệu từ server
    response = requests.get(url)

    # Kiểm tra mã trạng thái của phản hồi
    if response.status_code == 200:  # Mã trạng thái 200 đại diện cho thành công
        # Lấy dữ liệu từ phản hồi dưới dạng JSON
        data = response.json()

        # Xử lý dữ liệu theo nhu cầu của bạn
        # Ví dụ: lấy giá trị của trường "field1" trong dữ liệu
        field_values = [feed[f'field{field}'] for feed in data['feeds']]
        # Chọn giá trị khác None cuối cùng
        for i in range(len(field_values), 0, -1):
            if field_values[i-1] != None:
                return field_values[i-1]
        return get_data(field, number_of_data + 10)
    else:
        time.sleep(0.5)
        return get_data(field, number_of_data)

# Lấy dữ liệu từ ThingSpeak
fan_status = get_data(6, 20)
# temperature_status = get_data(1, 10)
# humidity_status = get_data(2, 10)

def publish_topic(topic, data, qos=0):
    results, mid = mqtt.publish(topic, data, qos=qos)
    print(results, mid)
    if results == 0:
        print("Message published successfully")
    else:
        time.sleep(1)
        return publish_topic(topic, data, qos=qos)
    return "OK"

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    # mqtt.subscribe(topic1)
    # mqtt.subscribe(topic2)
    # mqtt.subscribe(topic6)
    print('Connected to MQTT broker')

@mqtt.on_message()
def handle_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode('utf-8')
    print(f'Received message: {payload} on topic: {topic}')
    # if topic == topic1:
    #     global temperature_status
    #     temperature_status = payload
    #     print(temperature_status)
    # if topic == topic2:
    #     global humidity_status
    #     humidity_status = payload
    #     print(humidity_status)
    # if topic == topic6:
    #     global fan_status
    #     fan_status = payload
    #     print(fan_status)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/chart', methods=['GET'])
# def chart():
#     data = get_data()
#     return data

@app.route('/status', methods=['GET'])
def temperaturenow():
    return [get_data(1), get_data(2)]

# @app.route('/humiditynow', methods=['GET'])
# def humiditynow():
#     return humidity_status

@app.route('/fan', methods=['POST'])
def fan():
    data = request.data.decode('utf-8')
    print('\n')
    print(data)
    global fan_status
    if data == '1':
        fan_status = '1'
        publish_topic(topic6, '1', qos=0)
    else:
        if data == '0':
            fan_status = '0'
            publish_topic(topic6, '0', qos=0)
        else:
            return "ERROR"

    return "OK"

@app.route('/fanstatus', methods=['GET'])
def fanstatus():
    return fan_status

@app.route('/predict', methods=['GET'])
def predict():
    return render_template('detect.html')

@app.route('/predict/images', methods=['GET'])
def send_url_image():
    global image_urls
    image_urls = [
        'https://imagizer.imageshack.com/v2/256x256q90/r/922/qBS7oi.jpg',
        'https://imagizer.imageshack.com/img922/8630/N8qVTq.jpg',
        'https://imagizer.imageshack.com/v2/256x256q90/r/922/qBS7oi.jpg',
        'https://imagizer.imageshack.com/img922/8630/N8qVTq.jpg',
        'https://imagizer.imageshack.com/v2/256x256q90/r/922/qBS7oi.jpg'
    ]

    return json.dumps(image_urls)

@app.route('/predict/detect', methods=['GET'])
def detect():
    # detect_text = None
    with open('X:\Courses\IoTTechnologyAndApplications\Practice\FinalLab\detect\log\log_2023-06-19_13-52-31.json') as json_file:
        detect_text = json.load(json_file)
    # pre_text = process_text(detect_text)
    # print(pre_text)
    return detect_text

###################################################################################
if __name__ == '__main__':
    app.run(host="localhost" ,port=3001, debug=True)

###################################################################################



