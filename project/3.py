
#find out list of prime numbers:
import math
final_num=600851475143
#final_num=3135
p_list=[]
for num in range(1,int(math.sqrt(final_num))+1,2):
#for num in range(1,int(math.sqrt(final_num))+1,2):
    prime = True
   # for i in range(2,num):
    for i in range(2,int(math.sqrt(num))+1):
        if (num%i==0):
            prime = False
    if prime:
        p_list.append(num)
print (p_list)

##testing for range to check smaller endpoint
##for z in range(20,10,-1):
##    print (z)


f_list=[]
for val in p_list:
#    print (val)
    if final_num%val==0:
        f_list.append(val)
        

print (f_list)
       
    
