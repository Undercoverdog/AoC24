# Define the path to your file
file_path = 'input'

# Initialize two separate lists for the columns
first_column = []
second_column = []

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        # Strip any leading/trailing whitespace and split the line into two numbers
        num1, num2 = line.strip().split()
        # Append each number to the respective list as integers
        first_column.append(int(num1))
        second_column.append(int(num2))

# Print the result
#print("First Column:", first_column)
#print("Second Column:", second_column)


def radixsort_msb(arr, k=0):
    if k>31: return arr
    bucket0 = []
    bucket1 = []
    for i in range(0, len(arr)):
        nth_bit = (arr[i] >> k) & 1
        if nth_bit == 0:
            bucket0.append(arr[i])
        else:
            bucket1.append(arr[i])

    return radixsort_msb(bucket0 + bucket1, k+1)

l_sorted_perma = radixsort_msb(first_column)
r_sorted_perma = radixsort_msb(second_column)

l_sorted = l_sorted_perma[:]
r_sorted = r_sorted_perma[:]

result = 0
for i in range(0,len(l_sorted)):
    diff = l_sorted[i] - r_sorted[i]
    if diff<0: diff = -diff
    result += diff

print(result)


## Part 2

result = 0
for l in first_column:
    for r in second_column:
        if l == r: result+=l

print(result)