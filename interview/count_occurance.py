import pprint
max_item = None
data=[1]

print(len(data))

if len(data)!=0:
    map={}

    for key in data:
        if key not in map:
            map[key]=1
        else:
            map[key]+=1
            
    pprint.pprint(map)

    max_item =max(map, key=map.get)

    print(max_item)


print (max_item)


