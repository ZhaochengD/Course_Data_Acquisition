#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:04:28 2019

@author: zhaocheng_du
"""

from gtts import gTTS 
import warnings
import os 
warnings.filterwarnings("ignore")

class Speaker():
    def __init__(self, text):     
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False) 
        myobj.save("temp.mp3")
        os.system('/usr/local/bin/mpg321 temp.mp3') 
    
    def speakFiles(filename):
        os.system('/usr/local/bin/mpg321 ' + filename) 

if __name__ == "__main__":
    Speaker('Sorry, the parking lot is full')
    #Speaker('你好!')
