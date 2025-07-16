from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.layers import Layers
from kmk.extensions.display import DisplayExtension
from kmk.extensions.display.displayio_oled import DisplayIOOLED
from adafruit_displayio_ssd1306 import SSD1306

# Import your existing keymap layers
from config.keymap import layers

keyboard = KMKKeyboard()

# Add layers extension to support layers in your keymap
keyboard.extensions.append(Layers())

# Initialize and add the OLED display extension
display_ext = DisplayExtension(
    display_driver_class=SSD1306,
    i2c_addr=0x3C,  # Default OLED I2C address
    width=128,
    height=64,
)
keyboard.extensions.append(display_ext)

# Use your existing keymap layers
keyboard.keymap = layers

if __name__ == '__main__':
    keyboard.go()
