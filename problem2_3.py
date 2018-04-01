# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:32:17 2018

@author: dulck
"""

newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for i in range(0, len(ne)):
        print(ne[i] + " has " + str(len(ne[i])) + " letters.")