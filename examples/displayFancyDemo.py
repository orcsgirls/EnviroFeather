import board
import time
import terminalio
from adafruit_display_text import label
from displayio import OnDiskBitmap, TileGrid, Group

# Read image (once)
# The TFT display is 240x135 pixels
img = OnDiskBitmap("images/background.bmp")

# Simple counter to test
for i in range(100):
    main_group = Group()

    # image first
    tile_grid = TileGrid(bitmap=img, pixel_shader=img.pixel_shader)
    main_group.append(tile_grid)

    # Text
    text_area = label.Label(terminalio.FONT, text="ORCSEnviro",
                scale=2, color=0x00ff00, background_color=None)
    text_area.x = 10
    text_area.y = 10
    main_group.append(text_area)

    # Number
    text_area = label.Label(terminalio.FONT, text=str(i),
                scale=4, color=0xffff00, background_color=None)
    text_area.x = 40
    text_area.y = 70
    main_group.append(text_area)

    board.DISPLAY.show(main_group)

    # Sleep
    time.sleep(1.0)

input('Press any key to exit')
