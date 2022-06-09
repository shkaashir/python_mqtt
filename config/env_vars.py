from datetime import datetime
# from typing import Li, Dict
from pydantic import BaseSettings, ValidationError as pydantic_validation_error

class EnvVars(BaseSettings):
    mqtt_broker: str
    mqtt_user: str
    mqtt_password: str
    mqtt_port: int
    mqtt_topic: str
    mqtt_client_id: str

    class Config:
        env_file = "./../.env"
try:
    env = EnvVars()
    print(env.__dict__)
except pydantic_validation_error as e:
    print(e.json())

