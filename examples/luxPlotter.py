import time
import board
import adafruit_vcnl4040
import adafruit_bme680

#-------------------------------------------------------------------

i2c = board.I2C()

bme680   = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
vcnl4040 = adafruit_vcnl4040.VCNL4040(i2c)

#-------------------------------------------------------------------
# Measure
#-------------------------------------------------------------------

while True:

    # for plotting we print a tuple. ERach number is a new line on the plot

    print ((vcnl4040.lux,))
    time.sleep(0.5)
