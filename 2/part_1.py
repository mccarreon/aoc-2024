# levels must be ALL increasing or ALL decreasing
# adjacent levels must differ by ONE but no more than THREE

# input_file = '/home/mattc/aoc2/2/newinput.txt'
input_file = '/home/mattc/aoc2/2/input.txt'

with open(input_file, 'r') as file:
    lines = file.read().splitlines()
    report_list = [list(map(int, line.split())) for line in lines]

def validate_increment_amount(x: int, y: int) -> bool:
    if not x or not y:
        return False
    
    if x == y or abs(x - y) > 3:
        return False
    
    return True

def validate_direction(is_increasing: bool, previous_num: int, current_num: int) -> bool:
    if is_increasing:
        return previous_num < current_num
    else:
        return previous_num > current_num


safe_count = 0
for report in report_list:
    is_increasing = False
    report_length = len(report)

    if report_length < 2:
        safe_count += 1

    if report[0] < report[1]:
        is_increasing = True

    valid_increment = True
    valid_direction = True
    for i in range(1, report_length):
        if not validate_direction(is_increasing, report[i - 1], report[i]):
            valid_direction = False
            break

        if not validate_increment_amount(report[i - 1], report[i]):
            valid_increment = False
            break

    if valid_increment and valid_direction:
        safe_count += 1

print(safe_count)