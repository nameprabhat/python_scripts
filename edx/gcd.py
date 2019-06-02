# -*- coding: utf-8 -*-


"""
Created on Mon Oct 29 09:17:55 2018

@author: sunny

greated common divisor
"""
def gcdIter(a, b):
    if a < b :
        lower = a
        print ('taking lower value as' , lower)
    else:
        lower = b
        print ('taking lower value as' , lower)
        
    for i in range (lower,0,-1):
        #print (i)
        if a%i == 0 and b%i == 0:
            return i

                
print ('greatst comman value will be', gcdIter(1071,462))



   
    
    




    


    
    