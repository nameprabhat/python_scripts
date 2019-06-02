def minmax(l:list) -> tuple:
    maximum = l[0]
    minimum = l[0]
    for i in range(len(l)):
        if l[i] > maximum :
            maximum = l[i]
        if l[i] < minimum :
            minimum = l[i]
    return maximum,minimum

if __name__ == '__main__':
    l= [0,3,515,62,55]
    print (minmax(l))
    l= [-30,3,5.15,62,55]
    print (minmax(l))
    print(type (minmax(l)))
            
