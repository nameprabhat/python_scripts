# check if number is prime or not

def yesprime(number):
    if number < 2:
        return False
    for y in range(2,number):
    #for num in range(2,number//2,2):
        if number % y == 0:
           # print ('Not')            
            return False
    return True


# create a list with all prime numbers
p_list=[0]
###i =len(p_list)
##i = 0
##while len(p_list) <= 10000:
##    if yesprime(i):
##        p_list.append(i)
##        #print(i)
##    i += 1

# 2000000  --two million
i = 0
while int(p_list[-1]) < 2000000:
    if yesprime(i):
        p_list.append(i)
    i += 1

#removing last prime
del p_list[-1]

#printing a sum of all numbers
print('sum of all numbers is: ' + str(sum(p_list)))
