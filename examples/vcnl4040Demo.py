import time
import board
import adafruit_vcnl4040

#-------------------------------------------------------------------

i2c = board.I2C()
vcnl4040 = adafruit_vcnl4040.VCNL4040(i2c)

print ('Light:',vcnl4040.lux)
print ('Proximity:',vcnl4040.proximity)
