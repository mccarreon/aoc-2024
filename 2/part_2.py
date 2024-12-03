# levels must be ALL increasing or ALL decreasing
# adjacent levels must differ by ONE but no more than THREE

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

def validate_report(report: list) -> list:
    bad_idxs = set()
    is_increasing = False
    report_length = len(report)

    if report_length < 2:
        return True
    
    if report[0] < report[1]:
        is_increasing = True

    for i in range(1, report_length):
        if not validate_direction(is_increasing, report[i - 1], report[i]):
            bad_idxs.add(i)

        if not validate_increment_amount(report[i - 1], report[i]):
            bad_idxs.add(i)   

    return bad_idxs

# input_file = '/home/mattc/aoc2/2/newinput.txt'
input_file = '/home/mattc/aoc2/2/input.txt'

with open(input_file, 'r') as file:
    lines = file.read().splitlines()
    report_list = [list(map(int, line.split())) for line in lines]

safe_count = 0
for report in report_list:
    bad_idxs = validate_report(report)
    if not bad_idxs:
        safe_count += 1
        continue

    # adding first two indeces since validate_report skips them whoops
    bad_idxs.add(0) 
    bad_idxs.add(1)
    for idx in bad_idxs:
        new_report = report[:idx] + report[idx + 1:]
        if not validate_report(new_report):
            safe_count += 1
            break

print(safe_count)