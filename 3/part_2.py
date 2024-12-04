import re


input_file = '/home/mattc/aoc2/3/input.txt'

with open(input_file, 'r') as file:
    text = file.read()

pattern = r"(don't\(\))|(do\(\))|mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, text)

is_adding = True
answer_sum = 0
for match in matches:
    if match[0] != '':
        is_adding = False
    elif match[1] != '':
        is_adding = True
    elif match[2] != '':
        if is_adding:
            answer_sum += int(match[2]) * int(match[3])