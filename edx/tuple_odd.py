# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:23:15 2018

@author: sunny
"""

#test =('I', 'am', 'a', 'test', 'tuple')
#lenght=len(test)
#output=()
#y=0
#while lenght > 0:
#    for i in range(0,lenght,2):
#        output[y]=test[i]
#    y = y+1
#    lenght = lenght -1
#
#
#print (output)
#
#

##one line code
#def oddTuples(test):
#    return test[::2]



test =('I', 'am', 'a', 'test', 'tuple')
##below is also a valid method
#print(test[::2])

def oddTuples(test):
    rtup=()
    index=0
    
    while index <len(test):
        rtup += (test[index],)
        index=index+2
    return rtup

out=oddTuples(test)
print(out)














        

        

