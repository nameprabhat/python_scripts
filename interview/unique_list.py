import pprint
list1=[1, 3, 4, 6, 7, 9,1]
list2=[1, 3, 4, 6, 7, 9,1]
temp=[]
#map={}
output=[]
for i in list1:
    if i not in temp:
        temp.append(i)
    #if key not in map:
        #map[key]=1
print(temp)

for i in list2:
    if i in temp:
        output.append(i)
   # if key in map:
        #map[key]+=1
        #output.append(key)
        
        
#pprint.pprint(map)
print (output)
    
    
        
