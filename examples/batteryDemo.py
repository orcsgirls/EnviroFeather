import time
import board
import terminalio
import displayio

from adafruit_display_text import label
from adafruit_lc709203f import LC709203F, PackSize

# Create sensor object, using the board's default I2C bus.
battery_monitor = LC709203F(board.I2C())

# Update to match the mAh of your battery for more accurate readings.
# Can be MAH100, MAH200, MAH400, MAH500, MAH1000, MAH2000, MAH3000.
# Choose the closest match. Include "PackSize." before it, as shown.
battery_monitor.pack_size = PackSize.MAH500

#--------------------------------------------------------------

while True:
    v = "Voltage: {:.2f} V".format(battery_monitor.cell_voltage)
    p = "Percent: {:.2f} %".format(battery_monitor.cell_percent)
    # Line 1
    main_group = displayio.Group()
    text_area = label.Label(terminalio.FONT, text="ORCSEnviro Battery", 
                scale=2, color=0xffff00, background_color=None)
    text_area.x = 10
    text_area.y = 10
    main_group.append(text_area)

    # Line 2
    text_area = label.Label(terminalio.FONT, text=v+"\n"+p,
                scale=2, color=0x00ff00, background_color=None)
    text_area.x = 25
    text_area.y = 40
    main_group.append(text_area)

    # Display
    board.DISPLAY.show(main_group)

    time.sleep(5.0)
