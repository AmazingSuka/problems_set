# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:44:38 2018

@author: dulck
"""
def problem4_3(product, cost):
    """ Prints the product name in a space of 25 characters, left-justified
        and the price in a space of 6 characters, right-justified"""
    print("{0:<23}  ${1:6.2f}".format(product,cost))

