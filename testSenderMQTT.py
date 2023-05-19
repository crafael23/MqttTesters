import datetime
import paho.mqtt.client as mqtt
import random
import time
import json

# Definir las funciones de callbacks de conexión y publicación
def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: "+str(rc))

def on_publish(client, userdata, mid):
    print("Mensaje publicado")

# Crear una instancia de cliente MQTT
client = mqtt.Client()

# Asignar las funciones de callback de conexión y publicación
client.on_connect = on_connect
client.on_publish = on_publish

# Conectarse al broker de Mosquitto en localhost
client.connect("localhost", 1883, 60)


while True:
    
    #Agua
    ph= random.randint(1,100)
    nivel= random.choice([True, False])
    dataA = {
        "ph": ph,
        "nivel": nivel,
    }
    messageA = json.dumps(dataA)
    client.publish("Estado_Agua", messageA)
    
    #Riego
    Modulo1=random.choice([True, False])
    Modulo2=random.choice([True, False])
    Modulo3=random.choice([True, False])
    Modulo4=random.choice([True, False])
    dataR= {
        "Modulo1_estado": Modulo1,
        "Modulo2_estado": Modulo2,
        "Modulo3_estado": Modulo3,
        "Modulo4_estado": Modulo4,
    }
    messageR = json.dumps(dataR)
    client.publish("Estado_Riego", messageR)
    
    
    #Modulo
    temperatura1 = random.randint(1,100)
    humedad1 = random.randint(1,100)
    id=1
    dataM1 = {
        "Id": id,
        "temperatura": temperatura1,
        "humedad": humedad1,       
    }
    message = json.dumps(dataM1)
    client.publish("Estado_Modulo", message)

    time.sleep(2)

# Mantener la conexión MQTT activa
client.loop_forever()
