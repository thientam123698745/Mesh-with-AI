
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "mesh_light.h"

#define BLINK_GPIO 23

void blink_task()
{
    /* Configure the IOMUX register for pad BLINK_GPIO (some pads are
       muxed to GPIO on reset already, but some default to other
       functions and need to be switched to GPIO. Consult the
       Technical Reference for a list of pads and their default
       functions.)
    */
    // esp_rom_gpio_pad_select_gpio(BLINK_GPIO);
    /* Set the GPIO as a push/pull output */
    // gpio_set_direction(BLINK_GPIO, GPIO_MODE_OUTPUT);
    // while(1) {
    //     /* Blink off (output low) */
    //     gpio_set_level(BLINK_GPIO, 0);
    //     vTaskDelay(1000 / portTICK_PERIOD_MS);
    //     /* Blink on (output high) */
    //     gpio_set_level(BLINK_GPIO, 1);
    //     vTaskDelay(1000 / portTICK_PERIOD_MS);
    // }
    // vTaskDelete(NULL);
}

void ledinit()
{
    // xTaskCreate(blink_task, "blink_task", 1012, NULL, 5, NULL);
}
