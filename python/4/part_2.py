import re


input_file = '/home/mattc/aoc2/python/4/input.txt'
# input_file = '/home/mattc/aoc2/python/4/example.txt'
input_array = []

with open(input_file, 'r') as file:
    for line in file:
        input_array.append(list(line.strip()))

    
def find_targets(row: int, col: int, input_array: list, target_coords):
    row_len, col_len = len(input_array), len(input_array[0])
    targets = 'MS'

    if row < 0 or col < 0 or row >= row_len or col >= col_len:
        return
    
    current_char = input_array[row][col]
    if current_char in targets:
        target_coords[current_char].append((row, col))

def verify_xmas(target_coords: dict):
    m1, m2 = target_coords['M']
    a_x, a_y = target_coords['A'][0]

    dx = m1[0] - a_x
    dy = m1[1] - a_y

    diag_x = a_x - dx
    diag_y = a_y - dy

    diagonal = (diag_x, diag_y)
    if m2 == diagonal:
        return 0
    else:
        print(f'Here is M1 and calculated diagonal: {m1, diagonal}')
        return 1

answer_sum = 0
for row in range(len(input_array)):
    for col in range(len(input_array[row])):
        if input_array[row][col] == 'A':
            target_coords = {'M': [], 'S': [], 'A': [(row, col)]}
            # look at bottom left
            find_targets(row + 1, col - 1, input_array, target_coords)
            # look at bottom right
            find_targets(row + 1, col + 1, input_array, target_coords)
            # look at top left
            find_targets(row - 1, col - 1, input_array, target_coords)
            # look at top right
            find_targets(row - 1, col + 1, input_array, target_coords)
            if len(target_coords['M']) == 2 and len(target_coords['S']) == 2:
                print(target_coords)
                answer_sum += verify_xmas(target_coords)


print(answer_sum)