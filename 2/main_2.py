from to_array import *

counter = 0

with open('input', 'r') as f:
    for l in f:
        input = to_array(l)
        if len(input) <= 1: 
            counter+=1
            continue

        if input[0] == input[1]: continue

        if input[0] < input[1]: 
            for i in range (0, len(input)-1):
                if not (input[i] - input[i+1] >= -3 and input[i] - input[i+1] < 0): break
                if i == len(input)-2: counter+=1

        else:
            for i in range (0, len(input)-1):
                if not (input[i] - input[i+1] <= 3 and input[i] - input[i+1] > 0): break
                if i == len(input)-2: counter+=1
        
 

print(counter)