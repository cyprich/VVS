from u_thing_speak import ThingSpeak
import network
import time

# starting connecting to WiFi network

ssid = 'KTK-96385247'
password = 'Kopera00'

station = network.WLAN(network.STA_IF)

station.active(True)

print('connecting to network...')

if station.isconnected() == False:
    station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())
print()

# ending connecting to WiFi network

# starting work with thingspeak

THINGSPEAK_WRITE_API_KEY = 'R2LY068XK1MTKGH2'
THINGSPEAK_READ_API_KEY = '6SM10TGBXPDTDKDG'
CHANNEL_ID = '2531788'

thing_speak = ThingSpeak()
thing_speak.set_write_api_key(THINGSPEAK_WRITE_API_KEY)
thing_speak.set_read_api_key(THINGSPEAK_READ_API_KEY)
thing_speak.set_channel_id(CHANNEL_ID)

# getting general data from ThingSpeak
pom = thing_speak.gather_data(0)
if pom[0] == 0:
    print('general data:')
    print(pom[1])
    print(pom[1]['name'])
    print()
    
# gathering 10 previously send data to ThingSpeak
        
# pom = thing_speak.gather_data(10)
# if pom[0] == 0:
#     print('general data:')
#     print(pom[1])
#     print()
#     
#     print('previous data:')
#     for i in range(0,len(pom[2])):
#         print(pom[2][i])
#         print(pom[2][i]['field1'])
#         print(pom[2][i]['field2'])
        
        
variable1 = 1
variable2 = 50000   

while True:
    variable1 = variable1 + 1
    variable2 = variable2 - 1
    
    # sending data to ThingSpeak
    data = {'field1':variable1, 'field2':variable2}
    thing_speak.send_data(data)
    
    # getting lastly send data to ThingSpeak
    pom = thing_speak.gather_data(1)
    if pom[0] == 0:
        print('previous data:')
        for i in range(0,len(pom[2])):
            print(pom[2][i])
            print(pom[2][i]['field1'])
            print(pom[2][i]['field2'])
    
    time.sleep(20)