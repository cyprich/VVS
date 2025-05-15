import network
import ufirebase as firebase
import time

# starting connecting to WiFi network

ssid = '***'
password = '***'

station = network.WLAN(network.STA_IF)

station.active(True)

print('connecting to network...')

if station.isconnected() == False:
    station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

# ending connecting to WiFi network

# starting work with firebase

URL_ADDRESS = "***"

firebase.setURL(URL_ADDRESS)

variable1 = 1
variable2 = 50000

while True:
    variable1 = variable1 + 1
    variable2 = variable2 - 1
    
    # sending data to firebase
    firebase.put("var1", str(variable1), bg = False)
    firebase.put("var2", str(variable2), bg = False)
    
    # downloading data from firebase
    firebase.get("var1", "pom1" , bg = False)
    print(firebase.pom1)
    firebase.get("var2", "pom2" , bg = False)
    print(firebase.pom2)
    print()
    
    # sending data to firebase
    firebase.addto("var1xl", str(variable1), bg = False)
    firebase.addto("var2xl", str(variable2), bg = False)
    
    # downloading data from firebase
    firebase.get("var1xl", "pom1xl" , bg = False)
    for i in list(firebase.pom1xl.values()):
        print(i)
    print()
    
    firebase.get("var2xl", "pom2xl" , bg = False)
    for i in list(firebase.pom2xl.values()):
        print(i)
    print()
    
    # sending data to firebase
    firebase.addto("variables",{"variable1":variable1, "variable2":variable2}, bg = False)
    
    # downloading data from firebase
    firebase.get("variables", "pom3" , bg = False)
    for i in list(firebase.pom3.values()):
        for j in list(i.values()):
            print(j)
    print()
    
    # deleting data from the firebase
    firebase.put("var_del", 'aaa', bg = False)
    time.sleep(5)
    firebase.delete('var_del', bg = False)
    
    time.sleep(20)