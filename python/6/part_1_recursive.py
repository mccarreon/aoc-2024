input_file = '/home/mattc/aoc2/python/6/input.txt'
# input_file = '/home/mattc/aoc2/python/6/example.txt'

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

FACING_UP = '^'
FACING_DOWN = 'v'
FACING_RIGHT = '>'
FACING_LEFT = '<'

def turn_right(facing_direction: str) -> str:
    if facing_direction == FACING_UP:
        return FACING_RIGHT
    elif facing_direction == FACING_DOWN:
        return FACING_LEFT
    elif facing_direction == FACING_LEFT:
        return FACING_UP
    elif facing_direction == FACING_RIGHT:
        return FACING_DOWN

def find_guard_status(lab_map: list) -> dict:
    for row in range(len(lab_map)):
        for col in range(len(lab_map[row])):
            if lab_map[row][col] in [FACING_UP, FACING_DOWN, FACING_LEFT, FACING_RIGHT]:
                return { 'coordinates': [row, col], 'facingDirection': lab_map[row][col] }

def dfs(coordinates: list, facing_direction: tuple, lab_map: list) -> None:
    row_len = len(lab_map)
    col_len = len(lab_map[0])

    if coordinates[0] < 0 or coordinates[0] >= row_len or coordinates[1] < 0 or coordinates[1] >= col_len:
        return 'FINISH'
    
    if lab_map[coordinates[0]][coordinates[1]] == '#':
        return turn_right(facing_direction)

    if lab_map[coordinates[0]][coordinates[1]] == '.':
        lab_map[coordinates[0]][coordinates[1]] = 'X'
    
    if facing_direction == FACING_UP:
        new_direction = dfs([sum(x) for x in zip(coordinates, UP)], facing_direction, lab_map)
    elif facing_direction == FACING_DOWN:
        new_direction = dfs([sum(x) for x in zip(coordinates, DOWN)], facing_direction, lab_map)
    elif facing_direction == FACING_LEFT:
        new_direction = dfs([sum(x) for x in zip(coordinates, LEFT)], facing_direction, lab_map)
    elif facing_direction == FACING_RIGHT:
        new_direction = dfs([sum(x) for x in zip(coordinates, RIGHT)], facing_direction, lab_map)
    
    if new_direction and new_direction != 'FINISH':
        dfs(coordinates, new_direction, lab_map)
    else:
        print(lab_map)
        return

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