"""
    Quick and dirty MQTT door sensor
"""

import time
import network
import ubinascii
import machine
from umqttsimple import MQTTClient
import esp
import adcmode

try:
    import secrets
except:
    import secrets_sample as secrets

try:
    ### Create wifi network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    print("wifi: connecting")
    sta_if.connect(secrets.SSID, secrets.PASSWD) # Connect to an AP
    try:
        sta_if.ifconfig((secrets.IPADDR, secrets.MASK, secrets.GW, secrets.DNS))
    except:
        print("using DHCP...")

    ### Setup ADC to measure VCC
    if not adcmode.set_adc_mode(adcmode.ADC_MODE_VCC):
        print("ADC mdode changed in flash - restart needed")
        machine.reset()
    vcc = machine.ADC(1).read()/1024.0

    while not sta_if.isconnected():
        time.sleep(0.5)

    print("wifi connected: ", sta_if.ifconfig())


    ### connect to MQTT
    CLIENT_ID = ubinascii.hexlify(machine.unique_id())
    client = MQTTClient(CLIENT_ID, secrets.MQTT_SVR, user=secrets.MQTT_USER, password=secrets.MQTT_PWD )
    client.connect()
    print("mqtt: connected")
    payload = secrets.MQTT_PAYLOAD.format(vcc)
    client.publish(secrets.MQTT_TOPIC, payload)
    print("mqtt: published %s: %s"%(secrets.MQTT_TOPIC, payload))
    client.disconnect()
    print("mqtt: disconnected")
except Exception as e:
    print( "FATAL: ", type(e) )
    print( "       ", repr(e) )

time.sleep(0.1) # without this, deepsleep doesn't work well
esp.deepsleep(0)
