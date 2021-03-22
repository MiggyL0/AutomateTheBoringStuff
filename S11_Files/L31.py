# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:59:40 2020

@author: Miguel
"""

import os

os.chdir(r'C:\Users\Miguel\Documents\Programing Projects\AutomateTheBoringStuff')
print(os.getcwd())

helloFile = open(r'.\S11_Files\Hello.txt')
print(helloFile.read())

helloFile.close()

# helloFile = open(r'.\S11_Files\Hello.txt')



