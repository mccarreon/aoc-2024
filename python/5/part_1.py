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

input_file = '/home/mattc/aoc2/python/5/input.txt'
# input_file = '/home/mattc/aoc2/python/5/example.txt'

with open(input_file, 'r') as file:
    order_rules_text, update_text = file.read().split('\n\n')

update_array = create_update_array(update_text)
order_rules_dict = create_order_rules_dict(order_rules_text)

answer = 0
seen = set()
for update in update_array:
    for i in range(len(update)):
        if any(subsequent_nums in seen for subsequent_nums in order_rules_dict[update[i]]):
            seen = set()
            break
        elif i == len(update) - 1:
            answer += update[len(update) // 2]
            seen = set()
            break
        else:
            seen.add(update[i])

print(answer)