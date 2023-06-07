import paho.mqtt.client as mqtt
import random
import json
import threading
import time

# clases de modulos
class Module:
    def __init__(self, id: int, temperature: float, humidity: float, valve: bool):
        self.id = id
        self.temperature = temperature
        self.humidity = humidity
        self.valve = valve


modulo1 = Module(1, 0, 0, False)
modulo2 = Module(2, 0, 0, False)
modulo3 = Module(3, 0, 0, False)
modulo4 = Module(4, 0, 0, False)


# Definir las funciones de callbacks de conexión y publicación
def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: " + str(rc))


def on_publish(client, userdata, mid):
    print("Mensaje publicado")


# Crear una instancia de cliente MQTT
client = mqtt.Client()

# Asignar las funciones de callback de conexión y publicación
client.on_connect = on_connect
client.on_publish = on_publish

# Conectarse al broker de Mosquitto en localhost
client.connect("localhost", 1883,60 )


# Define the callback function for the subscription
def on_message(client, userdata, message):
    # Parse the received JSON message
    try:
        json_data = json.loads(message.payload.decode())
        data = json.loads(json_data['data'])
        module_id = data['moduleId']
        valve_value = data['value']
        print(f"Received message: Module ID : {module_id}, Valve Value - {valve_value}")
        
        match module_id:
            case 1:
                modulo1.valve = valve_value
            case 2:
                modulo2.valve = valve_value
            case 3:
                modulo3.valve = valve_value
            case 4:
                modulo4.valve = valve_value
        
        print(f"Module {module_id} valve value updated to {valve_value}")
        
        print(f"Module 1 valve value: {modulo1.valve}")
        print(f"Module 2 valve value: {modulo2.valve}")
        print(f"Module 3 valve value: {modulo3.valve}")
        print(f"Module 4 valve value: {modulo4.valve}")
        
    except KeyError:
        print("Received message does not contain the 'moduleId' key.")

def receive_messages():
    client.subscribe("modulo/valve")
    client.on_message = on_message
    client.loop_forever()



def send_messages():
    while True:
        modulo1.temperature = random.randint(1, 100)
        modulo1.humidity = random.randint(1, 100)
        dataM1 = {
            "moduleId": modulo1.id,
            "temperature": modulo1.temperature,
            "humidity": modulo1.humidity,
            "valve": modulo1.valve,
        }
        message = json.dumps(dataM1)
        client.publish("modulo/status", message)

        modulo2.temperature = random.randint(1, 100)
        modulo2.humidity = random.randint(1, 100)
        dataM2 = {
            "moduleId": modulo2.id,
            "temperature": modulo2.temperature,
            "humidity": modulo2.humidity,
            "valve": modulo2.valve,
        }
        message = json.dumps(dataM2)
        client.publish("modulo/status", message)

        modulo3.temperature = random.randint(1, 100)
        modulo3.humidity = random.randint(1, 100)
        dataM3 = {
            "moduleId": modulo3.id,
            "temperature": modulo3.temperature,
            "humidity": modulo3.humidity,
            "valve": modulo3.valve,
        }
        message = json.dumps(dataM3)
        client.publish("modulo/status", message)

        modulo4.temperature = random.randint(1, 100)
        modulo4.humidity = random.randint(1, 100)
        dataM4 = {
            "moduleId": modulo4.id,
            "temperature": modulo4.temperature,
            "humidity": modulo4.humidity,
            "valve": modulo4.valve,
        }
        message = json.dumps(dataM4)
        client.publish("modulo/status", message)    

        time.sleep(5)
        
        
send_thread = threading.Thread(target=send_messages)
receive_thread = threading.Thread(target=receive_messages)
send_thread.start()
receive_thread.start()
