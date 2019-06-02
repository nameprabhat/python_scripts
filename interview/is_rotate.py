def is_rotate(A,B):
    if len(A) != len(B):
        return False
    if len(A) == 0 or len(B) == 0:
        return False
    first = A[0]
    start = -123
##    if first in B:
##        start = B.index(first)
##    else:
##        return False
  
    for i in range(len(B)):
        if B[i] == first:
            start = i
            break
    if start == -123:
        return False
    
    new_B = B+B
    for i in range(1,len(A)):
        if A[i] != new_B[start +1]:
            return False
        start +=1
    return True


if __name__ == '__main__':
    
    A = [1, 2, 3, 4, 5, 6, 7]
    B = [4, 5, 6, 7, 8, 1, 2, 3]
    print(is_rotate(A,B))
    B = [4, 5, 6, 7, 1, 2, 3]
    print(is_rotate(A,B))
    A = [7, 1, 2]
    B = [ 5, 6, 7]
    print(is_rotate(A,B))
    B = [ 1, 2, 7]
    print(is_rotate(A,B))

    
