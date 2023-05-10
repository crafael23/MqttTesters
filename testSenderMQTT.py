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
    tiempoA = datetime.datetime.now()
    dataA = {
        "ph": ph,
        "nivel": nivel,
        "tiempo": tiempoA.strftime("%Y-%m-%d %H:%M:%S")
    }
    messageA = json.dumps(dataA)
    client.publish("Reserva_Agua", messageA)
    
    #Agua
    temperatura1 = random.randint(1,100)
    humedad1 = random.randint(1,100)
    date1 = datetime.datetime.now()
    dataM1 = {
        "temperatura": temperatura1,
        "humedad": humedad1,
        "tiempo": date1.strftime("%Y-%m-%d %H:%M:%S")        
    }
    message = json.dumps(dataM1)
    client.publish("modulo1", message)
    
    
    # temperatura2 = random.randint(1,100)
    # humedad2 = random.randint(1,100)
    # date2 = datetime.datetime.now()
    # dataM2 = {
    #     "temperatura": temperatura2,
    #     "humedad": humedad2,
    #     "tiempo": date2.strftime("%Y-%m-%d %H:%M:%S")
    # }
    # message2 = json.dumps(dataM2)
    # client.publish("modulo2", message2)
    
    
    # temperatura3 = random.randint(1,100)
    # humedad3 = random.randint(1,100)
    # date3 = datetime.datetime.now()
    # dataM3 = {
    #     "temperatura": temperatura3,
    #     "humedad": humedad3,
    #     "tiempo": date3.strftime("%Y-%m-%d %H:%M:%S")
    # }
    # message3 = json.dumps(dataM3)
    # client.publish("modulo3", message3)
    
    # temperatura4= random.randint(1,100)
    # humedad4 = random.randint(1,100)
    # date4= datetime.datetime.now()
    # dataM4={
    #     "temperatura": temperatura4,
    #     "humedad": humedad4,
    #     "tiempo": date4.strftime("%Y-%m-%d %H:%M:%S")
    # }
    # message4 = json.dumps(dataM4)
    # client.publish("modulo4", message4)

    time.sleep(5)

# Mantener la conexión MQTT activa
client.loop_forever()
