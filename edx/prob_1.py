
# gives the count of number of vowels
s = 'azcbobobegghakl'
vowels= ['a','e','i','o','u']
count=0
for char in s:
    if char in vowels:
        count +=1

print('Number of vowels: ' + str(count))
