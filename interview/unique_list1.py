def ff(l1,l2):
    new_ll = []
    for val in l1:
        if val in l2:
            new_ll.append(val)
    return new_ll
    

def ff_better(A,B):
    new_ll = []
    p1 = 0
    p2 = 0
    while p1 < len(A) and p2 < len(B):
        if A[p1] == B[p2]:
            new_ll.append(A[p1])
            p1 += 1
            p2 += 1
        elif A[p1] > B[p2]:
            p2 += 1
        else:
            A[p1] < B[p2]
            p1 += 1
    return new_ll




if __name__ == '__main__':
    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    print(ff(list_c1,list_c2))
    print(ff_better(list_c1,list_c2))
    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    print(ff(list_b1,list_b2))
    print(ff_better(list_b1,list_b2))
    
