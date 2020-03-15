from pyautogui import press, hotkey

windowsKey = {
    'start':    'playpause',
    'next':     'nexttrack',
    'back':     'prevtrack',
    'volup':    'volumeup',
    'voldown':  'volumedown',
    'mute':     'volumemute',
}

def dothis(key):
    if key == "close":
        hotkey('alt', 'f4')
    try:
        press(windowsKey[key])
        return True
    except KeyError:
        print(key)
        return False