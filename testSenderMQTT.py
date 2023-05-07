import paho.mqtt.client as mqtt
import random
import time

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
    # Generate two random values between 0 and 1 and save them to variables
    temperatura = random.randint(1,100)
    humedad = random.randint(1,100)
    

    messagetemp = str(temperatura)
    client.publish("modulo1/sensores/temperatura", messagetemp)

    messagehum = str(humedad)
    client.publish("modulo1/sensores/humedad", messagehum)

    time.sleep(2)
    
    # Ask the user if they want to continue the loop
    #user_input = input("Do you want to continue? (y/n) ")
    # # If the user enters anything other than 'y', exit the loop
    # if user_input.lower() != 'y':
    #     break

# Mantener la conexión MQTT activa
client.loop_forever()
