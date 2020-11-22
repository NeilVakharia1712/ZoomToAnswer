from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
import pyperclip

# Press and release space
def openChat():
    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    keyboard.press(Key.cmd.value)
    keyboard.press(Key.shift)
    keyboard.press('h')
    keyboard.release('h')
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd.value)

    for i in range(3):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    time.sleep(2)
    keyboard.press(Key.cmd.value)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.cmd.value)