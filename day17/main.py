from itertools import product
from operator import add

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def active_cubes(lines, dimension):
    result = set()
    for i, l in enumerate(lines):
        result.update({(i, j) + (0,) * dimension for j, c in enumerate(l) if c == '#'})
    return result

def get_nearby_positions(cube, dimension, iteration):
    result = set()
    for i in iteration:
        result.add(tuple(map(add, cube, i)))
    return result

def main(lines, dimension):
    actives = active_cubes(lines, dimension - 2)
    iteration = set(product(range(-1, 2), repeat=dimension))
    the_empty = (0,) * dimension
    iteration.remove(the_empty)
    for _ in range(6):
        new_actives = set()
        new_cubes = set()
        for x in actives:
            nearby = get_nearby_positions(x, dimension, iteration)
            if len([x for x in nearby if x in actives]) in [2, 3]:
                new_actives.add(x)
            new_cubes.update(nearby)
        inactives = new_cubes - actives
        for x in inactives:
            nearby = get_nearby_positions(x, dimension, iteration)
            if len([x for x in nearby if x in actives]) == 3:
                new_actives.add(x)
        actives = new_actives
    print(len(actives))

def main1():
    lines = list(read_file('input.txt'))
    main(lines, 3)

def main2():
    lines = list(read_file('input.txt'))
    main(lines, 4)
    
if __name__ == "__main__":
    main1()
    main2()
