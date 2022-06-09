from config.mq_config import MQTTProtocolConfig

def run():
    mqtt = MQTTProtocolConfig.getInstance()
    client = mqtt.connect_mqtt("pub_client_id")
    client.loop_start()
    mqtt.publish(client)


if __name__ == "__main__":
    run()