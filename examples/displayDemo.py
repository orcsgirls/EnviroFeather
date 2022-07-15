import time
import board
import terminalio
import displayio

from adafruit_display_text import label

#--------------------------------------------------------------
name = "Thomas :)"

# Line 1
main_group = displayio.Group()
text_area = label.Label(terminalio.FONT, text="ORCSEnviro", 
            scale=2, color=0xffff00, background_color=None)
text_area.x = 10
text_area.y = 10
main_group.append(text_area)

# Line 2
text_area = label.Label(terminalio.FONT, text=name, 
            scale=2, color=0x00ff00, background_color=None)
text_area.x = 50
text_area.y = 40
main_group.append(text_area)

# Display
board.DISPLAY.show(main_group)

# Key press to end
input('Press any key to end')