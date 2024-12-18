import math
import functools
from collections import Counter


input_file = 'input.txt'
# input_file = 'example.txt'

with open(input_file, 'r') as file:
    for line in file:
        stones = list(map(int, line.split()))

@functools.cache
def get_new_stone(stone: int) -> list:
    if stone == 0:
        return [1]
    
    num_digits = int(math.log10(stone)) + 1

    if num_digits % 2 == 0:
        str_stone = str(stone)
        first_half = int(str_stone[:num_digits//2])
        second_half = int(str_stone[num_digits//2:])
        return [first_half, second_half]
    
    return [stone*2024]

def blink(stone_freq: dict) -> list:
    new_freq = {}
    for stone, count in stone_freq.items():
        new_stones = get_new_stone(stone)
        for n_stone in new_stones:
            new_freq[n_stone] = new_freq.get(n_stone, 0) + count

    return new_freq
    
blinks = 25
freq = Counter(stones)
print(freq)
for i in range(blinks):
    freq = blink(freq)

print(sum(freq.values()))