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

time.sleep(0.1) # without this, deepsleep doesn't work well
esp.deepsleep(0)
