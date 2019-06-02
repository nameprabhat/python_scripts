def odd_mul(ll:list)->list:
    
    return [i for i in ll if i %2 != 0]

if __name__ == '__main__':
    ll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(odd_mul(ll))

            
    

