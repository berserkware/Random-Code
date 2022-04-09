import time
import math
import threading

def seconds_since_epoch():
    return int(str(math.floor(time.time() / 1000)) + "095")

start = int(1467195494)

initial_value = int(7070170)

rate = float(0.21756645758661888)

def render():
    return math.floor(initial_value + ((seconds_since_epoch() - start) * rate))

print(render())