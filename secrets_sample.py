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
MQTTSVR = "192.168.0.200"
MQTTUSER = "mqttuser"
MQTTPWD = "mqttpasswd"
MQTTTOPIC = "stat/door-01/door"
MQTTVALUE = "open"
