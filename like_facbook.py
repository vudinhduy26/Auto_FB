# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 16:33:23 2021

@author: duy
"""


from pynput.keyboard import Key, Controller
import time
a = 100
keyboard = Controller()
time.sleep(4.5)

while a>0:
    keyboard.press('j')
    keyboard.release('j')
    
    keyboard.press('l')
    keyboard.release('l')
        
    keyboard.press(Key.right)
    keyboard.release(Key.right)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    time.sleep(3)
    a -=1