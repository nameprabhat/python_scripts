# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:54:20 2019

@author: sunny
"""


#from datetime import datetime

a= [1,2,3,4,5,6,7]
b= [4,5,6,7,1,2,3]

def is_rotation(a,b):
    if len(a) != len(b):
        return False
    if a[0] not in b:
        return False
    else:
        index = b.index(a[0])
        rg = index + len(a)
        added = b + b
        i=0
        for val in range(index,rg):
            
            if added[val] != a[i]:
                return False
            i += 1
            
    return True

print(is_rotation(a,b))        

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
print(is_rotation(list1, list2a))  # should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
print(is_rotation(list1, list2b)) # should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
print( is_rotation(list1, list2c)) #should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
print(is_rotation(list1, list2d)) # should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
print( is_rotation(list1, list2e)) #should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
print (is_rotation(list1, list2f))   # should return True.

            
        


