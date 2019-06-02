# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:10:49 2018

@author: sunny
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * iterPower(base, exp-1)
    
    
print (iterPower(3,1))


def iterPower1(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        
        while exp  :
            result = base * result
            exp = exp -1
    return result


print (iterPower1(3,1))   
