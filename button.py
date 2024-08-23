import warnings
warnings.simplefilter('ignore')
from gpiozero import LED, Button
from signal import pause


led = LED(17)
button = Button(3)

button.when_pressed = led.on
button.when_pressed = led.off

pause()
