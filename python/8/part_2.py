import re


def create_order_rules_dict(order_rules_text):
    order_rules_array = order_rules_text.splitlines()
    order_rules_dict = {}

    for i in range(len(order_rules_array)):
        precedent, subsequent = tuple(map(int, order_rules_array[i].split('|')))
        if precedent not in order_rules_dict:
            order_rules_dict[precedent] = [subsequent]
        else:
            order_rules_dict[precedent].append(subsequent)

        if subsequent not in order_rules_dict:
            order_rules_dict[subsequent] = []

    return order_rules_dict

def create_update_array(update_text):
    update_text_array = update_text.splitlines()
    update_text_array = [list(map(int, line.split(','))) for line in update_text_array]
    return update_text_array

def bubble_sort(arr, order_rules_dict):
    n = len(arr)
    updated = False
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j+1] not in order_rules_dict[arr[j]]:
                updated = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr[n // 2] if updated else 0

input_file = '/home/mattc/aoc2/python/5/input.txt'
# input_file = '/home/mattc/aoc2/python/5/example.txt'

with open(input_file, 'r') as file:
    order_rules_text, update_text = file.read().split('\n\n')

update_array = create_update_array(update_text)
order_rules_dict = create_order_rules_dict(order_rules_text)

sum = 0
for update in update_array:
    sum += bubble_sort(update, order_rules_dict)

print(sum)