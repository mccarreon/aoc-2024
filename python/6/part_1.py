input_file = '/home/mattc/aoc2/python/6/input.txt'
# input_file = '/home/mattc/aoc2/python/6/example.txt'

directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def turn_right(direction: str) -> tuple:
    if direction == '^':
        return '>'
    elif direction == 'v':
        return '<'
    elif direction == '<': 
        return '^'
    elif direction == '>':
        return 'v'

def find_guard_status(lab_map: list) -> dict:
    for row in range(len(lab_map)):
        for col in range(len(lab_map[row])):
            if lab_map[row][col] in directions:
                return { 'coordinates': [row, col], 'facingDirection': lab_map[row][col] }

def dfs(start_coordinates: list, direction: str, lab_map: list) -> None:
    stack = [(start_coordinates, direction, start_coordinates)]
    row_len = len(lab_map)
    col_len = len(lab_map[0])
    
    while stack:
        coordinates, direction, old_coordinates = stack.pop()
        if coordinates[0] < 0 or coordinates[0] >= row_len or coordinates[1] < 0 or coordinates[1] >= col_len:
            continue
        
        if lab_map[coordinates[0]][coordinates[1]] == '#':
            new_direction = turn_right(direction)
            stack.append((old_coordinates, new_direction, coordinates))
            continue

        if lab_map[coordinates[0]][coordinates[1]] == '.' or lab_map[coordinates[0]][coordinates[1]] in directions:
            lab_map[coordinates[0]][coordinates[1]] = 'X'

        next_coordinates = [sum(x) for x in zip(coordinates, directions[direction])]

        stack.append((next_coordinates, direction, coordinates))

with open(input_file, 'r') as file:
    lab_map = [list(line) for line in file.read().splitlines()]

guard_status = find_guard_status(lab_map)

dfs((guard_status['coordinates']), guard_status['facingDirection'], lab_map)

visited = 1
for row in range(len(lab_map)):
    for col in range(len(lab_map[row])):
        if lab_map[row][col] == 'X':
            visited += 1

print(visited)