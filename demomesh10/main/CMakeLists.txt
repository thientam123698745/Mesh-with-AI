idf_component_register(SRCS "led.c" "client_post.c" "uart.c" "mqtt.c" "node_manager.c" "receive_data.c"
                            "mesh_main.c"
                    INCLUDE_DIRS "." "include")
target_compile_options(${COMPONENT_LIB} PRIVATE "-Wno-format")
