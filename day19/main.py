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

def make_regex(rules, key):
    t = []
    for rule in rules[key]:
        tmp = []
        for number in rule:
            if number.isdigit():
                tmp.append(make_regex(rules, number))
            else: # We find a rule like this : "a"
                tmp.append(number[1])
        t.append(''.join(tmp))
    return f"(?:{'|'.join(t)})"

def main1():
    lines = read_file(INPUT_FILE)
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
        
    regex = make_regex(cache, '0')
    print(sum(1 for x in messages if re.fullmatch(regex, x)))

def main2():
    lines = read_file(INPUT_FILE)
    
if __name__ == "__main__":
    main1()
    main2()

