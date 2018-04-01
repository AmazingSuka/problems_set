# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:54:14 2018

@author: dulck
"""

import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis = []
    for i in range(0,10):
        rand = random.random()
        rand = rand * 5 + 30
        lis.append(rand)
    print (lis)