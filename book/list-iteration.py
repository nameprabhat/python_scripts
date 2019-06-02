
import random
solutions=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121, 124, 127, 130, 133, 136, 139, 142, 145, 148, 151, 154, 157, 160, 163, 166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 205, 208, 211, 214, 217, 220, 223, 226, 229, 232, 235, 238, 241, 244, 247, 250, 253, 256, 259, 262, 265, 268, 271, 274, 277, 280, 283, 286, 289, 292, 295, 298, 301, 304, 307, 310, 313, 316, 319, 322, 325, 328, 331, 334, 337, 340, 343]

#cost=list()

#print (solutions)#
#print (len(solutions))

#for i in range(len(solutions)):
#    cost.append(random.randint(1,123))

#print (cost)
#print (len(cost))

costs=[87, 62, 37, 100, 120, 50, 42, 50, 120, 87, 64, 43, 19, 74, 50, 68, 33, 62, 28, 78, 32, 9, 69, 25, 55, 58, 55, 94, 102, 1, 117, 113, 69, 70, 30, 93, 114, 64, 101, 113, 58, 41, 70, 70, 60, 49, 16, 27, 112, 107, 89, 116, 24, 87, 68, 62, 11, 105, 42, 44, 109, 43, 109, 116, 63, 46, 95, 44, 58, 85, 13, 27, 89, 14, 40, 54, 28, 37, 91, 76, 48, 24, 2, 83, 65, 107, 72, 119, 101, 73, 47, 66, 83, 68, 120, 27, 14, 2, 34, 116, 2, 41, 117, 60, 75, 40, 86, 104, 38, 29, 51, 12, 14, 4, 61]

#### in this code block we have indentified highest value in list costs
high=0
for i in range(len(costs)):
    if costs[i]>=high:
        high=costs[i]
        print ('high value now #',high , 'index for it',i)

print ('final high value',high)

###### in this code block we have found out indexes for that heightet value

high_index=list()
for i in range(len(costs)):
    if high == costs[i]:
        print ('heightest value',high ,'is in index',i)
        high_index.append(i)


print ('here is your list',high_index)


##### now i have to find lowest values in 2nd list for these high values indexes:


rate=[1, 2, 3, 1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4,50, 68, 33, 62, 28, 78, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4,50, 68, 33, 62, 28, 78, 4, 1, 2, 3, 4, 1, 2, 3, 4,50, 68, 33, 62, 28, 78, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4,50, 68, 33, 62, 28, 78, 32, 9, 69, 25, 55, 58, 55, 94, 102, 1, 117, 113, 69, 70, 30, 93, 114, 64, 101, 113, 58, 41, 70, 70, 60, 49, 16, 27]
value=1000
for i in high_index:
    if rate[i]<=value:
        value=rate[i]
        index_value=i


print ('lowest value is :',value,'for index',index_value)


print(rate[4],rate[8],rate[94])
    
    

    



