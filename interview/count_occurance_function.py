
a=[int(x) for x in input('enter list:').split()]
print(a)

def most_frequent(given_list):
    max_item = None
    data = given_list
    if len(data)!=0:
        map={}

        for key in data:
            if key not in map:
                map[key]=1
            else:
                map[key]+=1
                
        
        max_item =max(map, key=map.get)
        
        return max_item


print(most_frequent(a))
