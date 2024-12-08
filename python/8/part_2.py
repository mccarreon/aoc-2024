from collections import deque


input_file = '/home/mattc/aoc2/python/8/input.txt'
# input_file = '/home/mattc/aoc2/python/8/example.txt'

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

with open(input_file, 'r') as file:
    city_map = [list(line.strip()) for line in file]

def is_inbounds(coords: tuple, city_map: list) -> bool:
    return coords[0] >= 0 and coords[0] < len(city_map) and coords[1] >= 0 and coords[1] < len(city_map[0])

def get_slope(coords: tuple, origin: tuple) -> tuple:
    row, col = coords
    origin_row, origin_col = origin

    d_row = row - origin_row
    d_col = col - origin_col

    return (d_row, d_col)

def find_antinodes(city_map: list, coords: tuple, origin_coords: tuple, placed_antinodes: list):
    [d_row, d_col] = get_slope(coords, origin_coords)
    
    queue = deque([origin_coords])
    visited = set([origin_coords])

    while queue:
        row, col = queue.popleft()
        placed_antinodes.add((row, col))

        left_coords = (row - d_row, col - d_col)
        if is_inbounds(left_coords, city_map) and left_coords not in visited:
            queue.append(left_coords)
            visited.add(left_coords)

        right_coords = (row + d_row, col + d_col)
        if is_inbounds(right_coords, city_map) and right_coords not in visited:
            queue.append(right_coords)
            visited.add(right_coords)

def bfs(city_map: list, origin_coords: tuple, frequency: str, placed_antinodes: list):
    queue = deque([origin_coords])
    visited = set([origin_coords])

    while queue:
        row, col = queue.popleft()
        
        if city_map[row][col] == frequency and (row, col) != origin_coords:
            find_antinodes(city_map, (row, col), origin_coords, placed_antinodes)

        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            
            if is_inbounds((new_row, new_col), city_map) and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

placed_antinodes = set()
visited_freqs = set()
for row in range(len(city_map)):
    for col in range(len(city_map[row])):
        if city_map[row][col] != '.' and (row, col) not in visited_freqs:
            bfs(city_map, (row, col), city_map[row][col], placed_antinodes)
            visited_freqs.add(city_map[row][col])

print(len(placed_antinodes))