def div(num):
    for i in range(2,21):
        if num%i!=0:
            return False
    return True


num=20

while True:
    if div(num):
        break
    num=num+20


print(num)
    
    
