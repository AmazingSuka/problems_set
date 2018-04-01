# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:01:31 2018

@author: dulck
"""

import csv
def problem3_7(csv_pricefile, flower):
    file = open(csv_pricefile)
    dict_ = {}
    cs = csv.reader(file)
    for row in cs:
        dict_[row[0]] = row[1]
    print(dict_[flower])