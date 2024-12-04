import re


input_file = '/home/mattc/aoc2/python/4/input.txt'
# input_file = '/home/mattc/aoc2/python/4/example.txt'
input_array = []

with open(input_file, 'r') as file:
    for line in file:
        input_array.append(list(line.strip()))

def find_xmas(row: int, col: int, target_idx: int, input_array: list, direction: str = 'ALL'):
    target = 'XMAS'
    target_letter = target[target_idx]
    row_len, col_len = len(input_array), len(input_array[0])
    
    if row < 0 or col < 0 or row >= row_len or col >= col_len:
        return 0

    current_char = input_array[row][col]
    if current_char != target_letter:
        return 0
    
    if target_letter == 'S':
        return 1
    
    if direction == 'ALL':
        return (
            find_xmas(row + 1, col, target_idx + 1, input_array, 'DOWN') + 
            find_xmas(row - 1, col, target_idx + 1, input_array, 'UP') + 
            find_xmas(row, col + 1, target_idx + 1, input_array, 'RIGHT') + 
            find_xmas(row, col - 1, target_idx + 1, input_array, 'LEFT') + 
            find_xmas(row + 1, col + 1, target_idx + 1, input_array, 'DOWN_RIGHT') + 
            find_xmas(row + 1, col - 1, target_idx + 1, input_array, 'DOWN_LEFT') + 
            find_xmas(row - 1, col + 1, target_idx + 1, input_array, 'UP_RIGHT') + 
            find_xmas(row - 1, col - 1, target_idx + 1, input_array, 'UP_LEFT')
        )
    elif direction == 'DOWN':
        return find_xmas(row + 1, col, target_idx + 1, input_array, 'DOWN')
    elif direction == 'UP':
        return find_xmas(row - 1, col, target_idx + 1, input_array, 'UP')
    elif direction == 'RIGHT':
        return find_xmas(row, col + 1, target_idx + 1, input_array, 'RIGHT')
    elif direction == 'LEFT':
        return find_xmas(row, col - 1, target_idx + 1, input_array, 'LEFT')
    elif direction == 'DOWN_RIGHT':
        return find_xmas(row + 1, col + 1, target_idx + 1, input_array, 'DOWN_RIGHT')
    elif direction == 'DOWN_LEFT':
        return find_xmas(row + 1, col - 1, target_idx + 1, input_array, 'DOWN_LEFT')
    elif direction == 'UP_RIGHT':
        return find_xmas(row - 1, col + 1, target_idx + 1, input_array, 'UP_RIGHT')
    elif direction == 'UP_LEFT':
        return find_xmas(row - 1, col - 1, target_idx + 1, input_array, 'UP_LEFT')

answer_sum = 0
for row in range(len(input_array)):
    for col in range(len(input_array[row])):
        if input_array[row][col] == 'X':
            answer_sum += find_xmas(row, col, 0, input_array)

print(answer_sum)