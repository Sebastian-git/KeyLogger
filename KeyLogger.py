from pynput.keyboard import Key, Listener
from threading import Thread
from pynput import keyboard
import time

stopCombo = {keyboard.Key.alt_l, keyboard.Key.down}
current = set()
keys = []

def on_press(key):
    print(key)
    store(key)
    if key in stopCombo:
        current.add(key)
        if all(k in current for k in stopCombo):
            listener.stop()

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def store(key):
    print(type(key))
    keys.append(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
