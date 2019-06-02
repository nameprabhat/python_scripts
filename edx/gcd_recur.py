# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:51:45 2018

@author: sunny

If b = 0, then the answer is a
 gcd(a, b) is the same as gcd(b, a % b)

"""
def gcdRecur(a, b):
    if b==0:
        return a
    else:
        print (a, b)
        return gcdRecur(b,a%b)
    
    
print ('greatst comman value will be', gcdRecur(10710000,462))

