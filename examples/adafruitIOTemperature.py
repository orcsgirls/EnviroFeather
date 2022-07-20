import time
import board
import ssl
import socketpool
import wifi
import adafruit_bme680
import adafruit_requests
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError

#-------------------------------------------------------------------
# Make sure you have secrets.py with the right credentials!
#-------------------------------------------------------------------
from secrets import secrets

aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
io = IO_HTTP(aio_username, aio_key, requests)

#-------------------------------------------------------------------
# Sensor
#-------------------------------------------------------------------
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

#-------------------------------------------------------------------
# Feeds
#-------------------------------------------------------------------
temperatureFeed = io.get_feed("temperature")

#-------------------------------------------------------------------

while True:
    t = bme680.temperature

    io.send_data(temperatureFeed["key"], t)
    print ("Temperature: ",t)

    time.sleep(10.0)
