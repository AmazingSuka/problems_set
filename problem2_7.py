# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 22:08:29 2018

@author: dulck
"""


def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter length of side one: " ))
    b = float(input("Enter length of side two: " ))
    c = float(input("Enter length of side three: " ))
    s = .5 * (a + b + c)
    area = (s * (s-a) * (s-b) * (s-c))**.5
    print("Area of a triangle with sides %.1f %.1f %.1f is %.1f" % (a,b,c,area))
