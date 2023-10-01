# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:52:38 2022

@author: Aishwarya Computers
"""


import random 
import string
'''lower = string.ascii_lowercase
upper = string.ascii_lowercase
digits= string.digits
symbols = string.punctuation

all = lower+upper+digits+symbols'''
all = string.printable
len =10
password = ''.join(random.sample(all,len))

print(password)