def div(num):
    for i in range(2,21):
        if num%i!=0:
            return False
    return True


num=2520 

while True:
    if div(num):
        break
    num=num+2520


print(num)
    
    
