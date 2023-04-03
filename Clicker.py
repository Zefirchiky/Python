from pynput.keyboard import Controller, Key, Listener
import pygame as pg
from time import sleep

keyboard = Controller()

i = 1
frase = "/changeme"

def on_press(key):
    if key == keyboard.Key.f6:
        print("F6 pressed. Stopping loop.")
        return False

print("Press F6 to stop the loop.")
run = True
sleep(5)

with Listener(on_press=on_press) as listener:
    while run:
        for i in frase:
            keyboard.press(i)
            sleep(.001)
            keyboard.release(i)
        keyboard.press(Key.enter)
        sleep(1)
        # keyboard.release(Key.enter)
        # for f in range(i):
        #     keyboard.press("0")
        #     sleep(.001)
        #     keyboard.release("0")
        # keyboard.press(Key.enter)
        # # sleep(.1)
        # keyboard.release(Key.enter)
        # for f in range(i):
        #     keyboard.press("O")
        #     # sleep(.001)
        #     keyboard.release("O")
        # keyboard.press(Key.enter)
        # # sleep(.1)
        # keyboard.release(Key.enter)
        # for f in range(i):
        #     keyboard.press("8")
        #     # sleep(.001)
        #     keyboard.release("8")
        # keyboard.press(Key.enter)
        # # sleep(.1)
        # keyboard.release(Key.enter)
        # i *= 2