import network
from time import sleep
from u_mqtt import Mqtt

# starting connecting to WiFi network

ssid = '***'
password = '***'

station = network.WLAN(network.STA_IF)

station.active(True)
if station.isconnected() == False:
    station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
print()

# ending connecting to WiFi network

# starting work with node_red

MQTT_SERVER_IP_ADDRESS = '*.*.*.*'

# we can create as much sub topics as we want to
# These are the MQTT OUT topics in the Node Red 
MQTT_SERVER_SUB_TOPIC_1 = '***'
MQTT_SERVER_SUB_TOPIC_2 = '***'

# we can create as much pub topics as we want to
# These are the MQTT IN topics in the Node Red
MQTT_SERVER_PUB_TOPIC_1 = '***'
MQTT_SERVER_PUB_TOPIC_2 = '***'

mqtt_object = Mqtt()

mqtt_object.set_mqtt_broker_ip_address(MQTT_SERVER_IP_ADDRESS)
mqtt_object.add_topic_sub(MQTT_SERVER_SUB_TOPIC_1)
mqtt_object.add_topic_sub(MQTT_SERVER_SUB_TOPIC_2)

while mqtt_object.connect_and_subscribe() != 0:
    pass
    sleep(1)

variable1 = 1
variable2 = 50000

while True:
    pom = mqtt_object.check_incomming_messages()
    if pom[0] == 0:
        print('received message topic: ' + pom[1])
        print('received message: ' + pom[2])
        print()
    
    mqtt_object.send_message(MQTT_SERVER_PUB_TOPIC_1, variable1)
    mqtt_object.send_message(MQTT_SERVER_PUB_TOPIC_2, variable2)

    variable1 = variable1 + 1
    variable2 = variable2 - 1
    
    sleep(5)