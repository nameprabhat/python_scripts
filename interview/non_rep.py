def non_rep(ss):
    dd = {}
    #single = []
    #temp = len(ss)
    for char in ss:
        if char in dd.keys():
            dd[char] += 1
        else:
            dd[char] = 1

    for char in ss:
        if dd[char] == 1:
            return char
    return None


##    for k,v in dd.items():
##        if v == 1:
##            single.append(k)
##    if len(single) == 0:
##            return None
##
##    for val in single:
##        if ss.index(val) < temp:
##            temp = ss.index(val)
##    return ss[temp]
##           
        
if __name__ == '__main__':
    
    ss = 'aabb'
    print(non_rep(ss))
    ss = 'abbzzzzzsdfag'
    print(non_rep(ss))
    ss = 'aadbbq'
    print(non_rep(ss))
    print(non_rep("aabbbcc"))
