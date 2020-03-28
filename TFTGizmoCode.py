import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo
from adafruit_circuitplayground.express import cpx
import time

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
"""splash = displayio.Group(max_size=10)
display.show(splash)"""

text_group = displayio.Group(max_size=2, scale=2, x=50, y=120)
# blank_text_area = label.Label(terminalio.FONT, text="                ", color=0xFFFFFF, background_color=0x000000)
# splash.append(text_group)
display.show(text_group)

def textUpdate(text):
    global text_group
    global blank_text_area
    try:
        text_group.pop()
    except:
        pass
 #   text_group.append(blank_text_area)  # Subgroup for text scaling
    time.sleep(2)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, background_color=0x000000)
    text_group.append(text_area)
  #  text_group.remove(blank_text_area)

while True:
    textUpdate("Hello World!")
    time.sleep(3)
    textUpdate("World!")
    time.sleep(3)
    textUpdate("Yay!")
    time.sleep(3)

while True:
    pass
