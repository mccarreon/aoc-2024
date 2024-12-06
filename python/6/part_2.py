import copy

# input_file = '/home/mattc/aoc2/python/6/input.txt'
input_file = '/home/mattc/aoc2/python/6/example.txt'

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
            
def check_cycle(start_coordinates: list, direction: str, lab_map: list, ans: list, visited: set) -> None:
    stack = [(start_coordinates, turn_right(direction), start_coordinates)]
    print(lab_map)
    row_len = len(lab_map)
    col_len = len(lab_map[0])
    cycle_check = set()
    while stack:
        coordinates, direction, old_coordinates = stack.pop()
        if coordinates[0] < 0 or coordinates[0] >= row_len or coordinates[1] < 0 or coordinates[1] >= col_len:
            continue
        
        if lab_map[coordinates[0]][coordinates[1]] == '#':
            new_direction = turn_right(direction)
            stack.append((old_coordinates, new_direction, coordinates))
            continue

        if (tuple(coordinates), direction) in cycle_check or (tuple(coordinates), direction) in visited:
            print('Found cycle at', coordinates, direction)
            ans[0] += 1
            return
        
        if lab_map[coordinates[0]][coordinates[1]] == '.' or lab_map[coordinates[0]][coordinates[1]] in directions:
            cycle_check.add(tuple((tuple(coordinates), direction)))

        next_coordinates = [sum(x) for x in zip(coordinates, directions[direction])]

        stack.append((next_coordinates, direction, coordinates))

def dfs(start_coordinates: list, direction: str, lab_map: list, ans: list) -> None:
    stack = [(start_coordinates, direction, start_coordinates)]
    row_len = len(lab_map)
    col_len = len(lab_map[0])
    visited = set()

    while stack:
        coordinates, direction, old_coordinates = stack.pop()
        if coordinates[0] < 0 or coordinates[0] >= row_len or coordinates[1] < 0 or coordinates[1] >= col_len:
            continue
        
        if lab_map[coordinates[0]][coordinates[1]] == '#':
            new_direction = turn_right(direction)
            stack.append((old_coordinates, new_direction, coordinates))
            continue

        if lab_map[coordinates[0]][coordinates[1]] == '.' or lab_map[coordinates[0]][coordinates[1]] in directions:
            visited.add(tuple((tuple(coordinates), direction)))

        next_coordinates = [sum(x) for x in zip(coordinates, directions[direction])]

        if not(next_coordinates[0] < 0 or next_coordinates[0] >= row_len or next_coordinates[1] < 0 or next_coordinates[1] >= col_len):
            print("Placing blockade at next coordinates: ", next_coordinates)
            copy_lab_map = copy.deepcopy(lab_map)
            copy_lab_map[next_coordinates[0]][next_coordinates[1]] = '#'
            check_cycle(coordinates, direction, copy_lab_map, ans, visited)

        stack.append((next_coordinates, direction, coordinates))

with open(input_file, 'r') as file:
    lab_map = [list(line) for line in file.read().splitlines()]

guard_status = find_guard_status(lab_map)
ans = [0]
dfs((guard_status['coordinates']), guard_status['facingDirection'], lab_map, ans)
print(ans)