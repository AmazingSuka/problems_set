# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:20:34 2018

@author: dulck
"""

def problem3_3(month, day, year):
    
    months = {1: "Junuary", 
              2: "February", 
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"}
    month = months[month]
    print(month, str(day) + ",", year)