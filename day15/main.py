from copy import deepcopy

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            return func(line.strip()) if func else line.strip()

class Test():
    def __init__(self):
        self.len = 0
        self.last = None
        self.last_last = None

    def insert(self, value):
        self.last_last = self.last
        self.last = value
        self.len += 1

def main(iteration):
    numbers = [int(x) for x in list(read_file('input.txt').split(','))]
    result = dict()
    prev = None
    for idx, key in enumerate(numbers):
        prev = key
        result.setdefault(key, Test()).insert(idx)
    for turn in range(len(numbers), iteration):
        value = 0
        if result[prev].len > 1:
            value = result[prev].last - result[prev].last_last
        result.setdefault(value, Test()).insert(turn)
        prev = value
    print(prev)

def main1():
    main(2020)

def main2():
    main(30000000)
    
if __name__ == "__main__":
    main1()
    main2()
