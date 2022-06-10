import time
import busio
import board
import adafruit_bme680
import ssl
import adafruit_requests
import socketpool
import wifi
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError

#-------------------------------------------------------------------
# Connect to Adafruit IO
#-------------------------------------------------------------------

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
io = IO_HTTP(aio_username, aio_key, requests)

def getFeed(name):
    try:
        feedID = io.get_feed(name)
    except RequestError:
        feed = Feed(name=name)
        feedID = io.create_new_feed(name)
    return feedID

#-------------------------------------------------------------------
# Measure
#-------------------------------------------------------------------

i2c = busio.I2C(board.SCL1, board.SDA1)  # Need to use the second I2C device (STEMMA connector)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
temperature_offset = -5

# Feeds

temperatureFeed = getFeed("temperature")
humidityFeed = getFeed("humidity")

while True:
    print("\nTemperature: %0.1f C" % (bme680.temperature + temperature_offset))
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    io.send_data(temperatureFeed["key"], bme680.temperature + temperature_offset)
    io.send_data(humidityFeed["key"],bme680.relative_humidity)

    time.sleep(60)
