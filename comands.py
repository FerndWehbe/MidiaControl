from pyautogui import press, hotkey
import webbrowser
import pyautogui
import re
import time

WINDOWSKEY = {
    "start": "playpause",
    "next": "nexttrack",
    "back": "prevtrack",
    "volup": "volumeup",
    "voldown": "volumedown",
    "mute": "volumemute",
    "fastnext": ["right"],
    "fastback": ["left"],
    "fullscreen": ["f"],
    "close": ["alt", "f4"],
    "closewin": ["ctrl", "w"],
}
FUNCTION = ["youtubemusic", "crunchyrollnext", "crunchyrollback"]


def dothis(key):
    if key in FUNCTION:
        if key == "youtubemusic":
            playmusic()
            return True
        else:
            crunchep(key[11:])
            print(key[11:0])
            return True
    try:
        if type(WINDOWSKEY[key]) == list:
            if len(WINDOWSKEY[key]) == 1:
                hotkey(WINDOWSKEY[key][0])
                return True
            else:
                hotkey(WINDOWSKEY[key][0], WINDOWSKEY[key][1])
                return True
        else:
            press(WINDOWSKEY[key])
            return True
    except KeyError:
        print(key)
        return False


def playmusic():
    webbrowser.get(
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    ).open_new_tab("music.youtube.com")
    titles = pyautogui.getAllTitles()
    sizescreenx1, sizescreeny1 = pyautogui.size()
    for title in titles:
        if re.search("Google Chrome", title):
            index_google = titles.index(title)
    win_title = pyautogui.getWindowsWithTitle(titles[index_google])[0]
    winx, winy = win_title.size
    time.sleep(4)
    if sizescreenx1 == 2560 and winx > 2000 and win_title.isMaximized:
        pyautogui.click(winx * 0.275, winy * 0.39)
    elif sizescreenx1 == 2560 and winx < 2000 and win_title.isMaximized:
        pyautogui.click(winx * 0.164 + sizescreenx1, winy * 0.525)
    else:
        pyautogui.click(winx * 0.164, winy * 0.525)


def crunchep(arg):
    titles = pyautogui.getAllTitles()
    for title in titles:
        if re.search("Crunchyroll", title):
            index_crunch = titles.index(title)
    win_title = pyautogui.getWindowsWithTitle(titles[index_crunch])[0]

    winx, winy = win_title.size
    sizescreenx1, sizescreeny1 = pyautogui.size()
    pyautogui.press("esc")
    if sizescreenx1 == 2560 and winx > 2000 and win_title.isMaximized:
        pyautogui.scroll(4000)
        if arg == "back":
            pyautogui.click(winx * 0.375, winy * 0.888)
        else:
            pyautogui.click(winx * 0.466, winy * 0.888)
    else:
        time.sleep(0.3)
        pyautogui.scroll(4000)
        time.sleep(0.3)
        pyautogui.scroll(-500)
        time.sleep(0.5)
        if sizescreenx1 == 2560 and winx < 2000 and win_title.isMaximized:
            if arg == "back":
                pyautogui.click(winx * 0.29 + sizescreenx1, winy * 0.70)
            else:
                pyautogui.click(winx * 0.45 + sizescreenx1, winy * 0.70)
        else:
            if arg == "back":
                pyautogui.click(winx * 0.183, winy * 0.70)
            else:
                pyautogui.click(winx * 0.45, winy * 0.70)
