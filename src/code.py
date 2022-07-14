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

print ("CHECKING SENSORS")

while True:
    print('===============================')
    print ('T:',bme680.temperature)
    print ('H:',bme680.relative_humidity)
    print ('P:',bme680.pressure)
    print ('VOC:',bme680.gas)
    print ('PROX:',vcnl4040.proximity)
    print ('LUX:',vcnl4040.lux)

    time.sleep(1.0)
