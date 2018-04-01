# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:52:50 2018

@author: dulck
"""

def problem3_1(txtfilename):
    file = open(txtfilename)
    count = 0
    for line in file:
        print(line, end= '')
        count+= len(line)
    print()
    print()
    print("There are %d letters in the file." % count)
        