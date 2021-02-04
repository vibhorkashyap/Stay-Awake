import pyautogui
import time
from datetime import datetime
from ctypes import Structure, windll, c_uint, sizeof, byref
import threading

pyautogui.FAILSAFE = False
idlesec = 600
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def checkIdle():
    threading.Timer(idlesec, checkIdle).start()
    while (1):
        idletime = 0
        while (idletime <= idlesec):
            idletime = get_idle_duration()
        for i in range(520,540):
            pyautogui.moveTo(990,i)
        pyautogui.press("shift")
        print("Movement made at {}" .format(datetime.now().time()))

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

checkIdle()





    







