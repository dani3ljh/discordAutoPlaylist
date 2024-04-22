from pynput.keyboard import Key, Controller
import keyboard
import random
import time
import sys

def pressAndRelease(controller: Controller, key: Key):
    controller.press(key)
    controller.release(key)

def macro(fileName: str, controller: Controller, isUsingBot: bool, cooldown = 3, botCommand = ",play"):
    print("macro activated")
    time.sleep(1)
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    random.shuffle(lines)
    for i in range(20):
        line = lines[i]
        if line.strip().startswith("//") or line.strip() == "":
            continue
        if isUsingBot:
            controller.type(botCommand + " ")
            controller.type(line)
            time.sleep(0.5)
            pressAndRelease(controller, Key.enter)
            time.sleep(cooldown)
            continue
        controller.type(line)
        time.sleep(0.5)
        pressAndRelease(controller, Key.enter)
        time.sleep(0.5)
        for _ in range(3):
            pressAndRelease(controller, Key.tab)
            time.sleep(0.5)
        pressAndRelease(controller, Key.enter)
        controller.press(Key.shift)
        time.sleep(0.5)
        for _ in range(3):
            pressAndRelease(controller, Key.tab)
            time.sleep(0.5)
        controller.release(Key.shift)
        pressAndRelease(controller, Key.backspace)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception("isUsingBot argument not given")
    fileName = 'songList.txt'
    controller = Controller()
    keyboard.add_hotkey('ctrl+shift+q', macro, args=(fileName, controller, bool(sys.argv[1])))
    while True:
        if keyboard.read_key() == "esc":
            break

