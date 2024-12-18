import copy

input_file = 'input.txt'
# input_file = 'example.txt'

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
            
def is_inbounds(coordinates: list, row_len: int, col_len: int) -> bool:
    return coordinates[0] >= 0 and coordinates[0] < row_len and coordinates[1] >= 0 and coordinates[1] < col_len

def is_cycle(start_coordinates: list, direction: str, lab_map: list, visited: set) -> None:
    print('looking for cycle')
    stack = [(start_coordinates, turn_right(direction), start_coordinates)]
    row_len = len(lab_map)
    col_len = len(lab_map[0])

    while stack:
        coordinates, direction, old_coordinates = stack.pop()
        vector = tuple((tuple(coordinates), direction))

        if not is_inbounds(coordinates, row_len, col_len):
            continue
        
        if lab_map[coordinates[0]][coordinates[1]] == '#' or lab_map[coordinates[0]][coordinates[1]] == 'O':
            new_direction = turn_right(direction)
            stack.append((old_coordinates, new_direction, coordinates))
            continue
        
        if vector in visited:
            pretty_print_lab_map(lab_map)
            print('Cycle detected!')
            return 1

        if lab_map[coordinates[0]][coordinates[1]] == '.' or lab_map[coordinates[0]][coordinates[1]] in directions:
            visited.add(vector)
            lab_map[coordinates[0]][coordinates[1]] = 'X'

        next_coordinates = [sum(x) for x in zip(coordinates, directions[direction])]

        stack.append((next_coordinates, direction, coordinates))

    pretty_print_lab_map(lab_map)
    return 0

def pretty_print_lab_map(lab_map):
    for row in lab_map:
        print(' '.join(row))
    print()  # Add an empty line for better readability

def dfs(start_coordinates: list, direction: str, lab_map: list) -> None:
    stack = [(start_coordinates, direction, start_coordinates)]
    row_len = len(lab_map)
    col_len = len(lab_map[0])
    cycle_count = 0
    visited = set()
    blockades_set = set()

    while stack:
        coordinates, direction, old_coordinates = stack.pop()
        vector = tuple((tuple(coordinates), direction))

        if coordinates[0] < 0 or coordinates[0] >= row_len or coordinates[1] < 0 or coordinates[1] >= col_len:
            continue
        
        if lab_map[coordinates[0]][coordinates[1]] == '#' or lab_map[coordinates[0]][coordinates[1]] == 'O':
            new_direction = turn_right(direction)
            stack.append((old_coordinates, new_direction, coordinates))
            continue

        if lab_map[coordinates[0]][coordinates[1]] == '.' or lab_map[coordinates[0]][coordinates[1]] in directions:
            visited.add(vector)
            lab_map[coordinates[0]][coordinates[1]] = 'X'

        next_coordinates = [sum(x) for x in zip(coordinates, directions[direction])]
        if is_inbounds(next_coordinates, row_len, col_len) \
            and lab_map[next_coordinates[0]][next_coordinates[1]] != '#'\
            and tuple(next_coordinates) not in blockades_set:
            
            lab_map_copy = copy.deepcopy(lab_map)
            lab_map_copy[next_coordinates[0]][next_coordinates[1]] = 'O'
            blockades_set.add(tuple(next_coordinates))
            pretty_print_lab_map(lab_map_copy)
            visited_copy = set(visited)
            cycle_count += is_cycle(coordinates, direction, lab_map_copy, visited_copy)

        stack.append((next_coordinates, direction, coordinates))
    
    return cycle_count

with open(input_file, 'r') as file:
    lab_map = [list(line) for line in file.read().splitlines()]

guard_status = find_guard_status(lab_map)
print(dfs((guard_status['coordinates']), guard_status['facingDirection'], lab_map))
