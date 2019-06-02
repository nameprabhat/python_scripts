#### try and except
###error handing

import sys
def divide42(value):
    try:
        return 42/value
    except ZeroDivisionError:
        print ('zero is not allowed')
    except TypeError:
        print ('input function needs to be converted in integer')
    except ValueError:
        print ('enter interger')
  


print (divide42(0))    
print (divide42(5))
print (divide42(10))
####commenting out below line to test except typerror
#num1 = int(input('enter number: '))
num1 = input('enter number: ')
print (divide42(num1))



print ('enter the number of cats')
num = input()


try:
    if int(num)>=4:
        print ('you have more than 4 cats')

    elif int(num)<0:
        print ('you have entered negative value...exiting the program')
        
    else:
        print ('you have less than 4 cats')
except:
    print ('you have not entered a number...exiting the program')
    




