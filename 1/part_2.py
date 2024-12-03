from collections import Counter

array_1 = []
array_2 = []

input_file = 'input.txt'

with open(input_file, 'r') as file:
    for line in file:
        parts = line.strip().split('   ')
        if len(parts) == 2:
            array_1.append(int(parts[0]))
            array_2.append(int(parts[1]))

array_2_count = Counter(array_2)

sum = 0
for num in array_1:
    sum += num * array_2_count[num]

print(sum)