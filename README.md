# upy-door-sensor
Dead simple MQTT door-sensor based on ESP8266 (ESP01) with MicroPython

Using `umqttsimple.py` from [MicroPython-Lib](https://github.com/micropython/micropython-lib)
package (author: Paul Sokolovsky, license: MIT License).<br>
A big thanks to MicroPython authors and contributors.

![photo should display here](https://raw.githubusercontent.com/barbudor/upy-door-sensor/master/hardware/photo1.jpg "photo")


# Principle of operation
The ESP8266 is maintained in permanent Deep Sleep state (do not connect GPIO16 to RESET).
A pulse is generated on RESET whenever the door opens and the switch closes, resulting in
waking up the ESP. Once awaken, the ESP8266 connects to the Wifi, the MQTT server and then
publish on a given topic before entering in Deep Sleep.

See hardware details in [`hardware/`](https://github.com/barbudor/upy-door-sensor/tree/master/harware)
folder. Schematics avaible for both:
- [Circuit-Diagram.org](https://www.circuit-diagram.org/editor/)
- [Fritzing](http://fritzing.org/)

![schematics should display here](https://raw.githubusercontent.com/barbudor/upy-door-sensor/master/hardware/circuit-diagram.org/upy-door-sensor.png "schematics")
You must use a micro-switch which is open when the door is closed and closed when the door is open.
A reed switch is not suitable.

The MQTT message include a status for the door (always "open" as the sensor cannot detect
closing the door) and the VCC voltage. As soon as it drops below the regulator voltage, it means
that the battery is low and should be changed/charged.

# Configuration
No fancy web-server!
Configuration is performed by renaming `secrets_sample.py` as `secrets.py` and entering your
parameters. Should be self-explanatory.

Build and enjoy !
