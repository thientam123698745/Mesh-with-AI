# Link tutorial: https://code.google.com/archive/p/imageshackapi/wikis/ImageshackAPI.wiki

"""
    Uploading an Image ( Basic )
    * Endpoint : https://post.imageshack.us/upload_api.php
    * Parameters :
    1. `*`    key : The api key for your application; found in email sent after filling out our <a href='http://imageshack.us/p/rules/'>API Key Request form</a>
    1. `*`    fileupload : image file
    1. `*` format : json
 """

"""
    Example Upload an Image ( Basic )
 """

import requests

def upload_image(api_key, image_path):
    upload_url = 'https://post.imageshack.us/upload_api.php'

    # Prepare the parameters
    params = {
        'key': api_key,
        'format': 'json'
    }

    # Prepare the files to be uploaded
    files = {
        'fileupload': open(image_path, 'rb')
    }

    # Send the POST request
    response = requests.post(upload_url, data=params, files=files)

    # Process the response
    if response.status_code == 200:
        response_json = response.json()
        # Handle the response JSON as needed
        print(response_json)
    else:
        print('Upload failed. Status code:', response.status_code)


# Sử dụng hàm upload_image
api_key = '256AIMXY27e3b11ddfdd68371c9efec7262f305d' # API key của bạn
image_path = 'img/1.JPG' # Đường dẫn tới ảnh cần upload

upload_image(api_key, image_path)



# Kết quả trả về
"""
    {'status': '1', 'version': 9, 'timestamp': 1687099383, 'base_url': 'https://imagizer.imageshack.com/', 'lp_hash': 'pmmrOBg4j', 'id': '1422046040', 'rating': {'ratings': 0, 'avg': 0}, 'files': {'server': 922, 'bucket': 2605, 'image': {'size': 10, 'content-type': 'image/jpeg', 'filename': 'mrOBg4.jpg', 'original_filename': '1.JPG'}, 'thumb': {'size': 0, 'content': 'image/jpeg', 'filename': 'mrOBg4.th.jpg'}}, 'resolution': {'width': 256, 'height': 256}, 'exif-info': {'exifimagesnum': '1', 'exiffilesize': '10'}, 'class': 'r', 'visibility': 'yes', 'uploader': {'ip': '115.78.15.113', 'cookie': '4ec46ba3e525462110a71dbb5db613de'}, 'links': {'image_link': 'https://imagizer.imageshack.com/img922/2605/mrOBg4.jpg', 'image_html': "<a href='https://imageshack.com/i/pmmrOBg4j' target='_blank'><img src='https://imagizer.imageshack.com/img922/2605/mrOBg4.jpg' alt='Free Image Hosting at www.imageshack.com' border='0'/></a>'", 'image_bb': '[URL=https://imageshack.com/i/pmmrOBg4j][IMG]https://imagizer.imageshack.com/img922/2605/mrOBg4.jpg[/IMG][/URL]', 'image_bb2': '[url=https://imageshack.com/i/pmmrOBg4j][img=https://imagizer.imageshack.com/img922/2605/mrOBg4.jpg][/url]', 'thumb_link': 'https://imagizer.imageshack.com/img922/2605/mrOBg4.th.jpg', 'thumb_html': "<a href='https://imageshack.com/i/pmmrOBg4j' target='_blank'><img src='https://imagizer.imageshack.com/img922/2605/mrOBg4.th.jpg' alt='Free Image Hosting at www.imageshack.com' border='0'/></a>'", 'thumb_bb': '[URL=https://imageshack.com/i/pmmrOBg4j][IMG]https://imagizer.imageshack.com/img922/2605/mrOBg4.th.jpg[/IMG][/URL]', 'thumb_bb2': '[url=https://imageshack.com/i/pmmrOBg4j][img=https://imagizer.imageshack.com/img922/2605/mrOBg4.th.jpg][/url]', 'is_link': 'https://imageshack.com/i/pmmrOBg4j', 'done': 'https://imageshack.com/i/pmmrOBg4j'}}
 """
# Xử lý phần kết quả trả về 'image_link'