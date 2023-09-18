from pynput.keyboard import Controller

import random
import time

key_press_dict = {
    0 : 'w',
    1 : 'a',
    2 : 's',
    3 : 'd'
}

# Virtual keyboard initialization
keyboard = Controller()

while True: # Loop until time depletes
    random_key_press = key_press_dict[random.randint(0,3)]
    print(random_key_press)
    keyboard.press(random_key_press)
    time.sleep(random.uniform(.18, .5))
    keyboard.release(random_key_press)