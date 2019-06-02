iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "PRABHAT SAXENA": 
        count += 1
        print(count)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
