from collections import Counter
import os

array_1 = []
array_2 = []

input_file = 'input.txt'

with open(input_file, 'r') as file:
    for line in file:
        parts = line.strip().split('   ')
        if len(parts) == 2:
            array_1.append(int(parts[0]))
            array_2.append(int(parts[1]))

array_1.sort()
array_2.sort()

sum = 0
for i in range(len(array_1)):
    sum += abs(array_1[i] - array_2[i])

print(sum)