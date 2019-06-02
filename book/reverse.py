def reverse(ll:list) ->list:
    return ll[-1::-1]


def reverse1(ll:list) ->list:
    re_ll = []
    for i in ll:
        re_ll.insert(0,i)
    return re_ll


if __name__ == '__main__':
    ll = [124,16,6,26.56,4]
    print(reverse(ll))
    print(reverse1(ll))
