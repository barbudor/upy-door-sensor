"""
    Your secrets and configurations items
    you must rename this file secrets.py and customize as needed
"""
# Wifi settings
SSID = "mywifi"
PASSWD = "thesecretpassword"
# Network - comment to use DHCP (but slighly slower)
IPADDR = "192.168.0.100"
MASK = "255.255.255.0"
GW = "192.168.0.1"
DNS = "1.1.1.1"
# MQTT settings
MQTT_SVR = "192.168.0.200"
MQTT_USER = "mqttuser"
MQTT_PWD = "mqttpasswd"
# Door status topic
MQTT_TOPIC = "stat/door1/STATUS"
MQTT_PAYLOAD = '{{"door":"open", "vcc":{:4.2f}}}'
