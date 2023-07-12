#include "mesh_light.h"
#include "driver/gpio.h"
bool Is_post_msg_not_null = 0;
char post_msg[CONFIG_MESH_ROUTE_TABLE_SIZE * 15] = "{";
int led = 0;
int BLINK_GPIO=0;
esp_err_t client_event_get_handler(esp_http_client_event_handle_t evt)
{
    switch (evt->event_id)
    {
    case HTTP_EVENT_ON_DATA:
        printf("HTTP_EVENT_ON_DATA: %.*s\n", evt->data_len, (char *)evt->data);
        break;
    case HTTP_EVENT_HEADER_SENT:
        {
            printf("HTTP_EVENT_HEADER_SENT: %.*s\n", evt->data_len, (char *)evt->data);
        }
        
        break;
    default:
        break;
    }
    return ESP_OK;
}

void rest_get(int * nodeid, char* temp)
{
    char *uri[100];
    sprintf(uri,"https://api.thingspeak.com/update?api_key=95Q6J6F9KGA8NXU6&field%d=%s",nodeid, temp);
    esp_http_client_config_t config_get = {
        .url = uri,
        .method = HTTP_METHOD_GET,
        .cert_pem = NULL,
        .event_handler = client_event_get_handler};
        
    esp_http_client_handle_t client = esp_http_client_init(&config_get);
    // esp_http_client_open(client, len);
    // esp_http_client_set_post_field(client, data, len);
    esp_http_client_perform(client);
    esp_http_client_cleanup(client);

}
void clientdata_analysis(char* data)
{
    char * feed = strstr(data, "feed");
    char * field1 = strstr(feed, "field1");
    char * data1 = strtok(field1, "\":,");
    data1 = strtok(NULL, "\":,");
    printf("data1: %s\r\n", data1);

}
esp_err_t client_event_get_handler2(esp_http_client_event_handle_t evt)
{
    switch (evt->event_id)
    {
    case HTTP_EVENT_ON_DATA:
        printf("HTTP_EVENT_ON_DATA: %.*s\n", evt->data_len, (char *)evt->data);
        clientdata_analysis(evt->data);
        // printf("led: %d\r\n", led);
        // led = led + 1;
        // if(led==1)
        // mesh_light_set(MESH_LIGHT_RED);
        // if(led==2)
        // mesh_light_set(MESH_LIGHT_GREEN);
        // if(led==3)
        // mesh_light_set(MESH_LIGHT_BLUE);
        // if(led==4)
        // mesh_light_set(MESH_LIGHT_YELLOW);
        // if(led==5)
        // mesh_light_set(MESH_LIGHT_PINK);
        // if(led==6)
        // mesh_light_set(MESH_LIGHT_INIT);
        // if(led==7)
        // {
        //     mesh_light_set(MESH_LIGHT_WARNING);
        //     led=1;
        // }
        esp_rom_gpio_pad_select_gpio(5);
        gpio_set_direction(5, GPIO_MODE_OUTPUT);
        esp_rom_gpio_pad_select_gpio(6);
        gpio_set_direction(6, GPIO_MODE_OUTPUT);
        esp_rom_gpio_pad_select_gpio(7);
        gpio_set_direction(7, GPIO_MODE_OUTPUT);
        esp_rom_gpio_pad_select_gpio(48);
        gpio_set_direction(48, GPIO_MODE_OUTPUT);
        gpio_set_level(48, 1);
    /* Get the rgb bits shifting the counter variable
         to the right and then masking with AND 0x1 */
    // bool r = (led  >> 2) & 1;  
    // bool g = (led  >> 1) & 1;
    // bool b = (led  >> 0) & 1; //shift 0, I know. Aesthetics and symmetry ;)
    bool r = 1;
    bool g = 1;
    bool b = 1;
    printf("i= %d | rgb bits = r:%d, g:%d, b:%d,\n", BLINK_GPIO, r, g, b);
        
        
        gpio_set_level(5, r);
        gpio_set_level(6, g);
        gpio_set_level(7, b);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        /* Blink on (output high) */
        gpio_set_level(5, 0);
        gpio_set_level(6, 0);
        gpio_set_level(7, 0);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
        BLINK_GPIO = BLINK_GPIO+1;
        break;
    case HTTP_EVENT_HEADER_SENT:
        {
            printf("HTTP_EVENT_HEADER_SENT: %.*s\n", evt->data_len, (char *)evt->data);
        }
        
        break;
    default:
        break;
    }
    return ESP_OK;
}
void rest_get2()
{
    char *uri[100];
    sprintf(uri,"https://api.thingspeak.com/channels/2170806/feeds.json?api_key=SFLX1ZM73XGZ4M2M&results=1");
    esp_http_client_config_t config_get = {
        .url = uri,
        .method = HTTP_METHOD_GET,
        .cert_pem = NULL,
        .event_handler = client_event_get_handler2};
        
    esp_http_client_handle_t client = esp_http_client_init(&config_get);
    // esp_http_client_open(client, len);
    // esp_http_client_set_post_field(client, data, len);
    esp_http_client_perform(client);
    esp_http_client_cleanup(client);
    
}