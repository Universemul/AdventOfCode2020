import itertools
import functools
import re
import math

from copy import deepcopy

INPUT_FILE = 'input.txt'
MAX_ROWS_INDEX = 9
MAX_COLUMNS_INDEX = 9

def read_file(filename, func=None):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(func(line.strip()) if func else line.strip())
    return result

class Tile:
    def __init__(self, key, lines):
        self.key = key
        self.data = lines

    def top(self):
        return self.data[0]

    def bottom(self):
        return self.data[-1]

    def left(self):
        return [x[0] for x in tile]

    def right(self):
        return [x[-1] for x in tile]

def main1():
    lines = read_file(INPUT_FILE)
    tiles = list()
    i = 0
    while i < len(lines):
        if lines[i].startswith('Tile'):
            key = lines[i].replace('Tile ', '').replace(':', '') 
            i += 1
            line = lines[i]
            tile = list()
            while line:
                tile.append(line)
                i += 1
                line = list(lines[i])
            i += 1
            tiles.append(Tile(key, tile))
    # Generate variations of a Tile:
    #    - rotate 90/180/270
    #    - Flip Horizontal/Vertical
    # For each tile, brute force to find if a tile have matching border 
    # It's Sunday and I don't want to implement it... 

def main2():
    lines = read_file(INPUT_FILE)
    
if __name__ == "__main__":
    main1()
    main2()
