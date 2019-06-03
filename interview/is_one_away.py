##def uniq(ss:str) -> str:   ## takes a string and return string containaing only unique chars
##    ll = [] ##intializing a emply list
##    for val in ss :  ## looping all characters in string
##        if val not in ll:  ## if char is not already added in list
##            ll.append(val)  ##appending that char in list
##    return ''.join(ll)  ##returning a string from list elements
##    
def is_one_away(ss:str,dd:str) -> bool:
    ''' takes 2 strings and returns if they are one change away'''
    if abs(len(ss) - len(dd)) > 1: ## if their length difference is more than 1
        return False  #return false
    elif len(ss) == len(dd):  ##if their length is equal
        return is_one_away_same_length(ss,dd)  ##return/call a function for checking same length
    elif len(ss) > len(dd) :
        return is_one_away_diff_length(ss,dd)  ##return/call a function for checking different length
    else:
        return is_one_away_diff_length(dd,ss)  ##return/call a function for checking same length --swap the parameters
    
def is_one_away_same_length(s1,s2) -> bool:
    p1 = 0  ## initialize a pointer
    #p2 = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:  ### if characters are not equal
            p1 +=1  ## increase the count
            if p1 > 1:  ## if count is more than 1 return False
                return False
    return True

##it will work if length of strings differ by 1--if more than 1 --- above command abs(len(ss) - len(dd)) > 1 will take care
def is_one_away_diff_length(s1, s2) -> bool:
    i = 0 # initialize a pointer
    p1 = 0# initialize a pointer
    while i < len(s2): # start a loop until last index of smaller string
        if s1[i + p1] == s2[i]:  ###if chars are equal than check next char in loop
            i += 1  

        else:  ###if chars are not equal than add error count by 1
            p1 += 1
            if p1 >1:  # if 2 chars are not equal than return False
                return False
    return True
            
      
if __name__ == '__main__':
    #print(is_one_away("abcde", "abcd"))
    print(is_one_away("abde", "abcde"))  # should return True
    print(is_one_away("a", "a"))  # should return True
    print(is_one_away("abcdef", "abqdef"))  # should return True
    print(is_one_away("abcdef", "abccef"))  # should return True
    print(is_one_away("abcdef", "abcde"))  # should return True
    print(is_one_away("aaa", "abc"))  # should return False
    print(is_one_away("abcde", "abc"))  # should return False
    print(is_one_away("abc", "abcde"))  # should return False
    print(is_one_away("abc", "bcc"))  # should return False
    print(is_one_away("aggbc", "ccccc"))  # should return False

            
        
