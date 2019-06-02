# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:58:39 2018

@author: sunny
"""

### recursion program for factorial

def factor(n):
    if n==1:
        return 1
    else:
        return n * factor(n-1)
    

value = factor(1101)
print (value)

