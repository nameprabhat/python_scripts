def uniq(ll) ->list:
    return list(set(ll))

def uniq1(ll) ->list:
    uniq_ll = []
    for i in ll:
        if i not in uniq_ll:
            uniq_ll.append(i)
    return uniq_ll
    

if __name__ == '__main__':
    ll = [12,12,34,56,262,62,87,34]
    print(ll)
    print(uniq(ll))
    print(uniq1(ll))
