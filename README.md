# upy-door-sensor
Dead simple MQTT door-sensor based on ESP8266 (ESP01) wiht MicroPython

`umqttsimple.py` is from [MicroPython Lib package](https://github.com/micropython/micropython-lib)
(author: Paul Sokolovsky, license: MIT License).<br>
A big thanks to MicroPython author and contributors.

# Principle of operation
The ESP8266 is maintained in permamenent Deep Sleep state (do not connect GPIO16 to RESET).
A pulse is generated on RESET whenever the door switch close, resulting in waking up the ESP.
Once awaken, the ESP8266 connects to the Wifi, the MQTT server and then publish on a given
topic before entering in Deep Sleep.

See schematics in [`hardware/`](https://github.com/barbudor/upy-door-sensor/tree/master/harware)
folder. Schematics created online using
[Circuit-Diagram.org](https://www.circuit-diagram.org/editor/)

![schematics should display here](https://raw.githubusercontent.com/barbudor/upy-door-sensor/master/hardware/upy-door-sensor.png "schematics")

You must use a normally-open micro-switch and not a reed switch (normally-closed).

# Configuration
No fancy web-server!
Configuration is performed by renaming `secrets_sample.py` as `secrets.py` and entering your
parameters. Should be self-explanatory.

Build and enjoy !
