import paho.mqtt.client as mqtt
import requests
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    msg = {}
    msg['counter'] = 10
    msg['device_id'] = 'ebba371354c14960a850ad98304d2004'
    msg['balance'] = 100
    data = json.dumps(msg)
    client.publish('eliot/update/ebba371354c14960a850ad98304d2004',data)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    device = (msg.topic).replace('eliot/update/','')
    print device
    print type(msg.payload)
    print json.dumps(msg.payload)
    print json.loads(msg.payload)
    
   # r = requests.post("http://127.0.0.1:8000/update/",data=msg.payload)
    #print r.text

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("139.59.79.221", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()