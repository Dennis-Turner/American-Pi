###
#Modified from 
#  https://learn.adafruit.com/adafruit-led-backpack/overview
#  I did not find Pi - Python images for the 8x8 
#  I humbly offer led8x8_images.py for that
# 
###

import time
import numpy as np
import sys

from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8
import led8x8_images as mycharacters

# Create display instance on default I2C address (0x70) and bus number.
# My test fixture has two 8x8 displays, 
display0 = Matrix8x8.Matrix8x8(address=0x70)
display2 = Matrix8x8.Matrix8x8(address=0x72)

#display.set_blinkrage(1)
# Initialize the display. Must be called once before using the display.
display0.begin()
display2.begin()

display0.set_brightness(4)
display2.set_brightness(2)

# Run through each pixel individually and turn it on.
for x in range(1):
	for y in range(8):
		# Clear the display buffer.
		display0.clear()
		display2.clear()
		# Set pixel at position x, y to on.  To turn off a pixel set
		# the last parameter to 0.
		display0.set_pixel(x, y, 1)
		display2.set_pixel(x, y, 1)
		# Write the display buffer to the hardware.  This must be called to
		# update the actual display LEDs.
		display0.write_display()
		display2.write_display()
		# Delay for a tenth of a second.
		time.sleep(0.1)

# address the arguments
# 
Z=0
Y=0

if len(sys.argv) > 1:
    Z=sys.argv[1]
if len(sys.argv) > 2:
    Y=sys.argv[2]

firstimage=mycharacters.test_matrix(Z)
secondimage=mycharacters.test_matrix(Y)

display0.set_image(firstimage)
display0.write_display()

display2.set_image(secondimage)
display2.write_display()
