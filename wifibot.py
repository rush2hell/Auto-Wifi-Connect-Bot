import os
import sys

saved_network = os.popen("netsh wlan show profiles").read()
print(saved_network)

list_network = os.popen("netsh wlan show networks").read()
print(list_network)

take_ssid = input("Enter SSID you want to connect: ")

disconnect = os.popen("netsh wlan disconnect").read()
print(disconnect)

if take_ssid not in saved_network:
    print("SSID : "+take_ssid+" is not present in available networks")
    print("Unable to establish connection")
    sys.exit()
else:
    print("Profile for"+take_ssid+" is saved in networks")

while True:
    available = os.popen("netsh wlan0 show networks").read()
    if take_ssid in available:
        print("Found")
        break

print("Connecting to "+take_ssid)
connect_cmd = os.popen("netsh wlan connect name='+'"'+preferred_ssid+'"").read()
print(connect_cmd)
