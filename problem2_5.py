# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:45:13 2018

@author: dulck
"""

import random

def problem2_5():
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    for i in range(0,10):
        print(random.randint(1,6))