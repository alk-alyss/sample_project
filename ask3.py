import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT Broker!")
	else:
		print("Failed to connect, return code %d\n", rc)

client = mqtt.Client()
client.on_connect = on_connect()

client.connect("mqtt.eclipseprojects.io")
client.loop_start()


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    data: str

@app.post("/")
def getMessage(message: Message):
	print(message.data)
	client.publish("alk_alyss/test", message)
