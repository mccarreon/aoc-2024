from collections import deque


input_file = 'input.txt'
# input_file = 'example.txt'

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
def is_inbounds(coords: tuple, arr: list) -> bool:
    return coords[0] >= 0 and coords[0] < len(arr) and coords[1] >= 0 and coords[1] < len(arr[0])

def bfs(trail_map: list, origin: tuple):
    queue = deque([origin])
    visited = set([origin])
    score = 0
    while queue:
        print(queue)
        row, col = queue.popleft()
        current_grade = trail_map[row][col]
        if current_grade == 9:
            score += 1
            continue

        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col

            if (
                is_inbounds((new_row, new_col), trail_map) and
                trail_map[new_row][new_col] == (current_grade + 1) 
                and (new_row, new_col, (origin[0], origin[1])) not in visited
            ):    
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
                            
    return score

with open(input_file, 'r') as file:
    trail_map = [list(map(int, list(line.strip()))) for line in file]

answer = 0
for row in range(len(trail_map)):
    for col in range(len(trail_map[row])):
        if trail_map[row][col] == 0:
            answer += bfs(trail_map, (row, col))
print(answer)

