from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)

for i in range(7819, 8000):
    keyboard.type(str(i))
    keyboard.press(Key.enter)
    time.sleep(0.5)
