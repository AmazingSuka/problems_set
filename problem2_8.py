# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 22:19:30 2018

@author: dulck
"""

def problem2_8(temp_list):
    sum_ = 0
    max_ = temp_list[0]
    min_ = max_
    for i in range(0,len(temp_list)):
        sum_ += temp_list[i]
        if min_ > temp_list[i]:
            min_ = temp_list[i]
        elif max_ < temp_list[i]:
            max_ = temp_list[i]
    avg = sum_ / len(temp_list)
    print("Average: " + str(avg))
    print("High: %.1f" % max_)
    print("Low: %.1f" % min_)    
    