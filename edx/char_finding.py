# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:01:10 2018

@author: sunny

Implement the function isIn(char, aStr) which implements the above idea recursively 
to test if char is in aStr. char will be a single character 
and aStr will be a string that is in alphabetical order. 
The function should return a boolean value.

    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise

NOT ABLE TO FIGURE OUT////DONE

"""

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   aStr = ''.join(sorted(set(aStr.lower())))
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   print (midChar)
   print (char)
   if char == midChar:
       return True
       
      # We found the character!
     
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
       return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])
    
    
print(isIn('g', 'gafhafkfakffaaezw'))  





    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
