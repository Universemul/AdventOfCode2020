import itertools
import functools
import re
import math

from collections import deque
from copy import deepcopy

INPUT_FILE = 'input.txt'

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result
class Game:
    def __init__(self, cups):
        self.cups = cups
        self.min_ = min(cups)
        self.max_ = max(cups)

    def take_3(self):
        result = []
        for _ in range(3):
            result.append(self.cups.popleft())
        return result
    
    def get_destination(self, current, take_values):
        destination = current - 1
        while True:
            if destination < self.min_:
                destination = self.max_
            if destination not in take_values:
                break
            destination = destination - 1
        return destination
    
    def move(self, destination, take_values):
        take_values.reverse()
        for x in take_values:
            self.cups.insert(self.cups.index(destination) + 1, x)

def main(depth, cups):
    g = Game(cups)
    for i in range(depth):
        current = g.cups[0]
        g.cups.rotate(-1)
        take_values = g.take_3()
        destination = g.get_destination(current, take_values)
        g.move(destination, take_values)
    one_index = g.cups.index(1)
    while one_index > 0:
        g.cups.rotate(-1)
        one_index -= 1
    return g

def main1():
    line = read_file(INPUT_FILE)[0]
    cups = deque([int(x) for x in line])
    g = main(100, cups)
    print(''.join([str(x) for idx, x in enumerate(g.cups) if idx > 0]))

def main2():
    line = read_file(INPUT_FILE)[0]
    cups = deque([int(x) for x in line])
    for x in range(max(cups) +1, 1000000):
        cups.append(x)
        g = main(1000000, cups) #TODO: Not working
    
if __name__ == "__main__":
    main1()
    main2()
