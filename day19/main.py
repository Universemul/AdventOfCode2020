import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'

def compute_inner_rules(value):
    if '"' in value:
        return [[value]] # no sub-rules
    if '|' in value:
        result = []
        groups = [x.strip() for x in value.split('|')]
        for x in groups:
            tmp = [r for r in x.split(' ')]
            result.append(tmp)
        return result
    return [[x for x in value.split(' ')]]
   
def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

def make_regex(rules, key, max_depth):
    t = []
    for rule in rules[key]:
        tmp = []
        for number in rule:
            if number.isdigit():
                if max_depth is None:
                    tmp.append(make_regex(rules, number, max_depth))
                else:
                    if number == key:
                        max_depth -= 1
                    if max_depth >= 0:
                        tmp.append(make_regex(rules, number, max_depth))
            else: # We find a rule like this : "a"
                tmp.append(number[1])
        t.append(''.join(tmp))
    return f"(?:{'|'.join(t)})"

def main(lines, max_depth):
    cache = dict()
    messages = []
    populate_messages = False
    for l in lines:
        if l == '':
            populate_messages = True
            continue
        if populate_messages:
            messages.append(l.strip())
        else:
            key, values = l.split(':')
            cache[key] = compute_inner_rules(values.strip())
        
    regex = make_regex(cache, '0', max_depth)
    print(sum(1 for x in messages if re.fullmatch(regex, x)))

def main1():
    lines = read_file(INPUT_FILE)
    main(lines, None)

def main2():
    lines = read_file(INPUT_FILE)
    for idx, x in enumerate(lines):
        if x == "8: 42":
            lines[idx] = "8: 42 | 42 8"
        elif x == "11: 42 31":
            lines[idx] = "11: 42 31 | 42 11 31"
    # Set max recursion because we can enter into a loop
    main(lines, 10) 


if __name__ == "__main__":
    main1()
    main2()

