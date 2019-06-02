def mul_20(ll:list)-> 'list or generator':
    new_ll = []
    for val in ll:
        if val not in new_ll:
            new_ll.append(val)
            for new_val in new_ll:
                if val * new_val == 20:
                    ###put return in here for returing only first pair
                    yield (val,new_val)
                    


    
    
if __name__ == '__main__':
    ll=[1,3,5,124,5124,514,12,3,4,1,2,10,20]
    print(type(mul_20(ll)))
    print (list(mul_20(ll)))
    ll=[1,20,5,124,5124,514,12,3,4,1,2,10]
    print(type(mul_20(ll)))
    print(mul_20(ll))
    
