# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:38:48 2018

@author: sunny

palindrome
"""

def ispad(s):
    if len(s) <= 1:
        print('yes')
        return True
    else:
        return s[0] == s[-1] and ispad(s[1:-1])

        
        
ispad('gaga')

