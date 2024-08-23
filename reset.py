from gpiozero import Button
from subprocess import call

def reset():
    print('button pressed')
    call([

button = Button(2)
button.when_pressed = reset()
button.wait_for_press()

