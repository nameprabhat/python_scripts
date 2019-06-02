def hello():
    print (123)
    print(2412)
    print(str(123) +' numbers')


hello()
hello()
hello()


print ('hello')
print ('world')
print ('hello', end = ' ')#### optional keyword arguments
print ('world')

print (123,24125,12421)
print (123,24125,12421,sep = 'Prabhat')#### optional keyword arguments


####local or global scope variables:
eggs=12324
def spam():
    global eggs ###########to assign global variable from inside of function
    eggs =11

spam()

print ('eggs global scope ' +str(eggs))

def milk():
    eggs=131
    bread()
    print ('eggs local scope ' +str(eggs))

def bread():
    eggs=444
    print ('this is from bread function')

milk()
