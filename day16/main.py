from functools import reduce

FILENAME = 'input.txt'

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def extract_bounds(line):
    result = []
    for v in line.split('or'):
        bounds = [int(x) for x in v.strip().split('-')]
        result.extend(bounds)
    return result

def get_rules(lines):
    rules = dict()
    for l in lines:
        if l == 'your ticket:' or l == "":
            break
        name, values = l.split(':')
        rules[name.strip()] = extract_bounds(values)
    return rules

def is_invalid(values, rules):
    sum_ = 0
    for v in values:
        names = next((key for key, value in rules.items() if value[0] <= v <= value[1] or value[2] <= v <= value[3]), None)
        if not names:
            sum_ += v
    return sum_

def get_values(value, rules):
    return {key for key, v in rules.items() if is_valid_for_a_rule(value, v)}

def main():
    lines = list(read_file(FILENAME))
    rules = get_rules(lines)
    start = False
    ratio = 0
    valid_tickets = []
    for l in lines:
        if l.strip().startswith("nearby tickets"):
            start = True
            continue
        if not start or l == "":
            continue
        values = [int(x) for x in l.strip().split(',')]
        tmp_ratio = is_invalid(values, rules)
        if tmp_ratio:
            ratio += tmp_ratio
        else:
            valid_tickets.append([int(x) for x in l.split(',')])
    return ratio, valid_tickets, rules

def is_valid_for_a_rule(value, rule):
 return rule[0] <= value <= rule[1] or rule[2] <= value <= rule[3]

def main2(tickets, rules):
    my_ticket = []
    lines = list(read_file(FILENAME))
    for idx, l in enumerate(lines):
        if l.startswith('your ticket'):
            my_ticket = [int(x) for x in lines[idx+1].split(',')]
            break
    result = {
        x: set() for x in range(len(my_ticket))
    }
    for key, values in rules.items():
        for i in range(len(my_ticket)):
            if all(is_valid_for_a_rule(x[i], values) for x in tickets):
                result[i].add(key)
    # Now, we have for each position, every field possibles

    order = [None] * len(my_ticket)
    total = 0
    for x in range(len(order)):
        for i in range(len(my_ticket)):
            if len(result[i]) == 1 and order[i] is None:
                break
        field = result[i].pop()
        order[i] = field
        # Remove field in other result
        for j in range(len(result)):
            if field in result[j]:
                result[j].remove(field)
    print(reduce(lambda x, y: x * y, [a for idx, a in enumerate(my_ticket) if order[idx].startswith('departure')]))

if __name__ == "__main__":
    ratio_invalid_tickets, valid_tickets, rules = main()
    print(ratio_invalid_tickets)
    main2(valid_tickets, rules)
