from .env_vars import env
from paho.mqtt import client as mqtt_client
import time

class MQTTProtocolConfig:
    
    __instance = None

    @staticmethod
    def getInstance():
        if MQTTProtocolConfig.__instance == None:
            MQTTProtocolConfig()

        return MQTTProtocolConfig.__instance

    def __init__(self) -> None:
        if MQTTProtocolConfig.__instance is not None:
            raise Exception("MQTT is a singleton class")
        else:
            self.broker = env.mqtt_broker
            self.port = env.mqtt_port
            self.topic = env.mqtt_topic
            self.client_id = env.mqtt_client_id
            self.username = env.mqtt_user
            self.password = env.mqtt_password
            MQTTProtocolConfig.__instance = self

    def connect_mqtt(self, client_id):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT successfully")
            else:
                print("Unable to connect to mqtt")
    
        client = mqtt_client.Client(client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def publish(self, client):
        msg_count = 0

        while True:
            time.sleep(2)
            msg = f"messages: {msg_count}"
            result = client.publish(self.topic, msg)
            if result[0] == 0:
                print(f"Send {msg} to topic {self.topic}")
            else:
                print(f"Failed to send message to topic {self.topic}")
            msg_count += 1


    def subscribe(self, client):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        client.subscribe(self.topic)
        client.on_message = on_message

    

if __name__ == "__main__":
    mqtt = MQTTProtocolConfig.getInstance()
    client = mqtt.connect_mqtt()
    client.loop_forever()
    mqtt.publish(client)


    # def __init__(self) -> None:
        