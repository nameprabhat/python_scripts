def sum_square(i:int) -> int:
    ll = [y for y in range(i)]
    ll = list(map (lambda x : x*x ,ll))
    return sum(ll[1:])

def sum1(ll):
    if len(ll) < 2 :
        return ll[0]
    sum = ll[0] + sum1(ll[1:])
    return sum
def squ(z):
    return z * z
    

def sum_square1(i:int) -> int:
    ll = [y for y in range(i)]
    new_ll= []
    for val in ll:
        new_ll.append(squ(val))
        
    #ll = list(map (lambda x : x*x ,ll))
    return sum1(new_ll[1:])

def sum_square_odd(i:int) -> int:
    ''' adding only odd squares'''
    ll = [y for y in range(i) if y%2 != 0]
    ll = list(map (lambda x : x*x ,ll))
    return sum(ll)

if __name__ == '__main__':
    print (sum_square(2))
    print (sum_square(24))
    print (sum_square(9))
    print (sum_square1(2))
    print (sum_square1(24))
    print (sum_square1(9))
    print (sum_square_odd(2))
    print (sum_square_odd(24))
    print (sum_square_odd(9))

