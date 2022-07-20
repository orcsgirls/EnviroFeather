import time
import board
import ssl
import socketpool
import wifi
import terminalio
import displayio

import adafruit_bme680
import adafruit_requests
from adafruit_display_text import label
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError

#-------------------------------------------------------------------
# Some helper routines
#-------------------------------------------------------------------
def getFeed(name):
    try:
        feedID = io.get_feed(name)
    except AdafruitIO_RequestError:
        feedID = io.create_new_feed(name)
    return feedID

#-------------------------------------------------------------------
def updateScreen(t,h,p):

    values = f"Temp: {t:.1f} C\nHum:  {h:.1f} %\nPress: {p:.0f} hPa"  
    main_group = displayio.Group()
    text_area = label.Label(terminalio.FONT, text="ORCSEnviro", 
                scale=2, color=0xffff00, background_color=None)
    text_area.x = 10
    text_area.y = 10
    
    main_group.append(text_area)
    
    text_area = label.Label(terminalio.FONT, text=values, 
                scale=2, color=0x00ff00, background_color=None)
    text_area.x = 50
    text_area.y = 40

    main_group.append(text_area)
    
    board.DISPLAY.show(main_group)
    return

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

#-------------------------------------------------------------------
# Measure
#-------------------------------------------------------------------

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

# Feeds

temperatureFeed = getFeed("temperature")
humidityFeed = getFeed("humidity")
pressureFeed = getFeed("pressure")

# Update times

start_time   = time.time()
current_time = start_time

update_data = 60.0
update_lcd  = 3.0

#-------------------------------------------------------------------
# Measure
#-------------------------------------------------------------------

while True:
    t = bme680.temperature
    h = bme680.relative_humidity
    p = bme680.pressure
    
    gas = bme680.gas   # Need some conversion here!
    alt = bme680.altitude

    updateScreen(t,h,p)
    
    if ((int (current_time - start_time) % update_data) == 0):
        io.send_data(temperatureFeed["key"], t)
        io.send_data(humidityFeed["key"], h)
        io.send_data(pressureFeed["key"], p)
            
    current_time = time.time()
    time.sleep(update_lcd)
