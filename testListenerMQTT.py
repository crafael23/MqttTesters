import paho.mqtt.client as mqtt

# Definir la función de callback de conexión
def on_connect(client, userdata, flags, rc):
    print("Conectado con resultado de código: "+str(rc))
    # Suscribirse al tópico 'test' después de conectarse
    client.subscribe("test")

# Definir la función de callback de recepción de mensajes
def on_message(client, userdata, msg):
    print("Mensaje recibido en el tópico 'test': "+msg.payload.decode())

# Crear una instancia de cliente MQTT
client = mqtt.Client()

# Asignar las funciones de callback de conexión y recepción de mensajes
client.on_connect = on_connect
client.on_message = on_message

# Conectarse al broker de Mosquitto en localhost
client.connect("192.168.1.24", 1883)

# Mantener la conexión MQTT activa y esperar a recibir mensajes
client.loop_forever()
