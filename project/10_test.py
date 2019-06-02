# check if number is prime or not
import math
def yesprime(number):

    if number %2 ==0 and number !=2 :
        return False
    if number %3 ==0 and number !=3 :
        return False
    if number %5 ==0 and number !=5 :
        return False
    if number %7 ==0 and number !=7 :
        return False
    if number %11 ==0 and number !=11 :
        return False
   # if number < 2 :
    #    return False
    
    for y in range(3,int(math.sqrt(number) + 1), 2):
    #for num in range(2,number//2,2):
        if number % y == 0:
           # print ('Not')            
            return False
    return True


# create a list with all prime numbers
p_list=[0]
n_list=[]


# 2000000  --two million
i = 101
while int(n_list[-1]) < 1000:
    if yesprime(i):
        p_list.append(i)
    i += 1

#removing last prime
del p_list[-1]

#printing a sum of all numbers
print (p_list)
# 1060 is sum for 1st hundred prime numbers
print('sum of all numbers is: ' + str(sum(p_list) + 1060))
