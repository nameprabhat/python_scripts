def mul_ll(ll1,ll2):
    ll3 = []
    for i in range(len(ll1)):
        ll3.append(ll1[i]*ll2[i])
    ll4 = [ll1[i]*ll2[i] for i in range(len(ll1))]
    ##return ll3 or ll4 both will have same values , for loop and list compre examples
    return ll4



if __name__ == '__main__':
    aa = [0, 2, 6, 12, 20, 30, 42, 56, 7220]
    bb= [12, 6, 42, 2, 56, 30, 72, 90, 0, 20,23]
    print (aa ,bb)
    print(mul_ll(aa,bb))
        
