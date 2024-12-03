from to_array import *

counter = 0




def check_inc(input, free=1):
    for i in range (0, len(input)-1):
        if not (input[i] - input[i+1] >= -3 and input[i] - input[i+1] < 0):
            if free==1:
                # Remove the i-th element
                arr1 = input[:i] + input[i+1:]

                # Remove the (i-1)-th element (only if i > 0)
                if i > 0:
                    arr2 = input[:i-1] + input[i:]
                else:
                    arr2 = input[:]  # If i is 0, no removal

                # Remove the (i+1)-th element (only if i+1 < len(input))
                if i + 1 < len(input):
                    arr3 = input[:i+1] + input[i+2:]
                else:
                    arr3 = input[:]  # If i+1 is out of bounds, no removal

                return check_inc(arr1,0) or check_inc(arr2,0) or check_inc(arr3,0)
            else: return False
    return True

def check_dec(input, free=1):

    for i in range (0, len(input)-1):
        if not (input[i] - input[i+1] <= 3 and input[i] - input[i+1] > 0): 
            if free==1:
                # Remove the i-th element
                arr1 = input[:i] + input[i+1:]

                # Remove the (i-1)-th element (only if i > 0)
                if i > 0:
                    arr2 = input[:i-1] + input[i:]
                else:
                    arr2 = input[:]  # If i is 0, no removal

                # Remove the (i+1)-th element (only if i+1 < len(input))
                if i + 1 < len(input):
                    arr3 = input[:i+1] + input[i+2:]
                else:
                    arr3 = input[:]  # If i+1 is out of bounds, no removal

                return check_dec(arr1,0) or check_dec(arr2,0) or check_dec(arr3,0)
            else: return False
    return True


with open('input', 'r') as f:
    for l in f:
        input = to_array(l)
        if len(input) <= 1: 
            counter+=1
            continue

        if(check_dec(input) or check_inc(input)): counter+=1

        
 

print(counter)