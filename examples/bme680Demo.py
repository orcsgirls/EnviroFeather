import time
import board
import adafruit_bme680

#-------------------------------------------------------------------

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)

print('===============================')
print ('T:',bme680.temperature)
print ('H:',bme680.relative_humidity)
print ('P:',bme680.pressure)
print ('VOC:',bme680.gas)
