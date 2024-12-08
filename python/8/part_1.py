from collections import deque


input_file = '/home/mattc/aoc2/python/8/input.txt'
# input_file = '/home/mattc/aoc2/python/8/example.txt'

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, -1),
    (1, 1),
    (-1, -1),
    (-1, 1)
]

with open(input_file, 'r') as file:
    city_map = [list(line.strip()) for line in file]

def is_inbounds(coords: tuple, city_map: list) -> bool:
    return coords[0] >= 0 and coords[0] < len(city_map) and coords[1] >= 0 and coords[1] < len(city_map[0])

def get_inverse_coordinates(coords: tuple, origin: tuple) -> tuple:
    row, col = coords
    origin_row, origin_col = origin
    
    inverse_row = 2 * origin_row - row
    inverse_col = 2 * origin_col - col
    
    return (inverse_row, inverse_col)

def bfs(city_map: list, origin_coords: tuple, frequency: str, antinode_coords: list):
    queue = deque([origin_coords])
    visited = set([origin_coords])

    while queue:
        row, col = queue.popleft()
        inverse_coordinates = get_inverse_coordinates((row, col), origin_coords)
        
        if city_map[row][col] == frequency \
            and (row, col) != origin_coords \
            and is_inbounds(inverse_coordinates, city_map)\
            and inverse_coordinates not in antinode_coords:
            
            print('found antinode for frequency', frequency, 'at', inverse_coordinates)
            antinode_coords.append(inverse_coordinates)

        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            if is_inbounds((new_row, new_col), city_map) \
                and (new_row, new_col) not in visited \
                and is_inbounds(get_inverse_coordinates((new_row, new_col), origin_coords), city_map):

                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

antinode_coords = []
for row in range(len(city_map)):
    for col in range(len(city_map[row])):
        if city_map[row][col] != '.':
            print('found frequency', city_map[row][col], 'at', (row, col))
            bfs(city_map, (row, col), city_map[row][col], antinode_coords)

print(len(antinode_coords))

