"""
    Quick and dirty MQTT door sensor
"""

import time
import network
import ubinascii
import machine
from umqttsimple import MQTTClient
import esp

try:
    import secrets
except:
    import secrets_sample as secrets

### Create wifi network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
print("wifi: connecting")
sta_if.connect(secrets.SSID, secrets.PASSWD) # Connect to an AP
try:
    sta_if.ifconfig((secrets.IPADDR, secrets.MASK, secrets.GW, secrets.DNS))
except:
    print("using DHCP...")

while not sta_if.isconnected():
    time.sleep(0.5)

print("wifi connected: ", sta_if.ifconfig())

### connect to MQTT
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
client = MQTTClient(CLIENT_ID, secrets.MQTTSVR, user=secrets.MQTTUSER, password=secrets.MQTTPWD )
client.connect()
print("mqtt: connected")
client.publish(secrets.MQTTTOPIC, secrets.MQTTVALUE)
print("mqtt: published")
client.disconnect()
print("mqtt: disconnected")

### can we go deepsleep ?
#test_in  = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
#test_out = machine.Pin(1, machine.Pin.OUT)
#test_out.value(0)
#disable_deepsleep = (test_in.value() == 0)
#if disable_deepsleep:
#    raise KeyboardInterrupt

time.sleep(0.1)
esp.deepsleep(0)
