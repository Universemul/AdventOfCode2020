import math

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def floor(value, min_):
    return math.floor(value - (value - min_) / 2)

def ceil(value, max_):
    return math.ceil(value + (max_ - value) / 2)

class Context:

    def __init__(self):
        self.max_row = 127
        self.min_row = 0
        self.max_col = 7
        self.min_col = 0
        self.last_row = None
        self.last_col = None
    
    def _consume_row(self, letter):
        if letter == 'F':
            self.max_row = floor(self.max_row, self.min_row)
        elif letter == 'B':
            self.min_row = ceil(self.min_row, self.max_row)
        self.last_row = letter

    def _consume_col(self, letter):
        if letter == 'L':
            self.max_col = floor(self.max_col, self.min_col)
        elif letter == 'R':
            self.min_col = ceil(self.min_col, self.max_col)
        self.last_col = letter

    def consume(self, letter):
        if letter in ['F', 'B']:
            self._consume_row(letter)
        else:
            self._consume_col(letter)

    def row_position(self):
        return math.floor(self.min_row)
    
    def col_position(self):
        return math.ceil(self.max_col)

def main1():
    lines = read_file('input.txt')
    max_count = 0
    ids = []
    for line in lines:
        context = Context()
        for l in line:
            context.consume(l)
        row = context.row_position()
        col = context.col_position()
        max_count = max(max_count, (row*8) + col)
        ids.append((row*8)+col)
    print(max_count)
    print(find_missing_seat(sorted(ids)))

# Basic binary search to find the missing integer in a sorted array
def find_missing_seat(seats):
    start = 0
    end = len(seats) - 1
    mid = 0
    while end > start + 1: 
        mid = (start + end) // 2
        if (seats[start] - start) != (seats[mid] - mid): 
            end = mid 
        elif (seats[end] - end) != (seats[mid] - mid): 
            start = mid 
    return seats[mid] + 1

if __name__ == "__main__":
    main1()
