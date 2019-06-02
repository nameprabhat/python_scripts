# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:43:55 2019

@author: sunny
"""

class Address(object):
    def __init__(self, number, streetName):
        self.number = number
        self.streetName = streetName
        # Line 1: Creating a number attribute
        # Line 2: Creating a streetName attribute  
        
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock1 = Clock('5:30')
clock1.print_time()



        
            