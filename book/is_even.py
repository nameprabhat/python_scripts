def is_even(n:int) -> bool:
    if n%2 == 0:
        return True
    return False


if __name__ == '__main__':
    print (is_even(2))
    print (is_even(34))
    print (is_even(-33))
    print (is_even(0.34))
    print (is_even(789))
    print (is_even(788))

    
