def is_mul(n:int,m:'integer') -> bool:
    if n%m == 0:
        return True
    return False

if __name__ == '__main__':
    print(is_mul(1,2))
    print(is_mul(2,5))
    print(is_mul(4,2))
    print(is_mul(4,2))
    print(is_mul(-10,5))
