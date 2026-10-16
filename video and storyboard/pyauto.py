import pyautogui
from time import sleep
from random import random as r
sleep(5)
with open("src/tmscli/main.py",'r') as script:
    # print(script)
    script=script.read()
    for i in script:
        pyautogui.write(i)
        if i in [" ","\n"]:
            if i=='\n':
                pyautogui.write('\n')
            x=r()
            sleep(x)

