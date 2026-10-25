import pyautogui
from time import sleep
from random import random as r
sleep(5)
with open("src/tmscli/main.py",'r') as script:
    # print(script)
    script=script.read()
    scripts=script.split('\n')
    cur=0
    for i in scripts:
        x=str(i)
        i.lstrip()
        diff=len(x)-len(i)
        diff/=3
        if i[:3]=='   ':
            pyautogui.press('tab')
            i=i[3:]


