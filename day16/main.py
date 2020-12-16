def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def get_rules(lines):
    rules = dict()
    for l in lines:
        if l == 'your ticket:' or l == "":
            break
        name, values = l.split(':')
        for v in values.split('or'):
            bounds = [int(x) for x in v.strip().split('-')]
            rules[(bounds[0], bounds[1])] = name.strip()
    return rules

def is_invalid(values, rules):
    sum_ = 0
    for v in values:
        names = next((key for key, value in rules.items() if key[0] <= v <= key[1]), None)
        if not names:
            sum_ += v
    return sum_

def main():
    lines = list(read_file('input.txt'))
    rules = get_rules(lines)
    start = False
    ratio = 0
    invalid_tickets = []
    for l in lines:
        if l.strip().startswith("nearby tickets"):
            start = True
            continue
        if not start or l == "":
            continue
        values = [int(x) for x in l.strip().split(',')]
        tmp_ratio = is_invalid(values, rules)
        if tmp_ratio:
            invalid_tickets.append(l)
            ratio += tmp_ratio
    return ratio, invalid_tickets 

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    ratio_invalid_tickets, invalid_tickets = main()
    print(ratio_invalid_tickets)
    main2(invalid_tickets)
