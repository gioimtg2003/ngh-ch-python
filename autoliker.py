from pynput.keyboard import Key, Controller
import time

time.sleep(4)
kbd = Controller()
kbd.press('j')
kbd.release('j')
time.sleep(1)

kbd.press('1')
kbd.release('1')
time.sleep(1)

kbd.press(Key.enter)
kbd.release(Key.enter)
