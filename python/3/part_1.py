import re


input_file = '/home/mattc/aoc2/3/input.txt'

with open(input_file, 'r') as file:
    text = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, text)

int_matches = [(int(x), int(y)) for x, y in matches]

answer = 0
for pair in int_matches:
    answer += pair[0] * pair[1]

print(answer)