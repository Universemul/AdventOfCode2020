import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

allergens = dict()
ingredients = list()
matching = dict()
found_allergens_ingredients = set()

def main(lines):
    for l in lines:
        ingred, ag = [x.strip() for x in l.split('(contains')]
        ingred = set(ingred.split(' '))
        ingredients.extend(ingred)
        ag = [x.strip() for x in ag.replace(')', '').split(',')]
        for x in ag:
            if x not in allergens:
                allergens[x] = deepcopy(ingred)
            else:
                allergens[x] &= ingred
    for a in sorted(allergens, key=lambda x: len(allergens[x])):
        tmp = deepcopy(allergens[a])
        if len(allergens[a]) > 1:
            tmp -= found_allergens_ingredients
        found_allergens_ingredients.update(tmp)

def main1():
    lines = read_file(INPUT_FILE)
    main(lines)
    print(len([x for x in ingredients if x not in found_allergens_ingredients]))

def main2():
    lines = read_file(INPUT_FILE)
    main(lines)
    dangerous = deepcopy(allergens)
    i = 0
    while i < len(dangerous):
        for key, v in dangerous.items():
            if len(v) > 1:
                continue
            for x in dangerous:
                if x == key:
                    continue
                dangerous[x] = dangerous[x] - dangerous[key]
            i += 1
    order = ','.join([dangerous[x].pop() for x in sorted(dangerous)])
    print(order) 

if __name__ == "__main__":
    main1()
    main2()
