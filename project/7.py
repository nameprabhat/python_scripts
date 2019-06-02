
### function to check if number is prime or not
#import math
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
p_list=[]
#i =len(p_list)
i = 0
while len(p_list) <= 10000:
    if yesprime(i):
        p_list.append(i)
        #print(i)
    i += 1
#print list
print (len(p_list))
print(p_list[-1])


for it in range(0,len(p_list)+1):
    print (p_list[it])
        
        
        
    
    
    


