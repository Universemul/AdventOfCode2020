from copy import deepcopy

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            return func(line.strip()) if func else line.strip()

def main(iteration):
    numbers = [int(x) for x in list(read_file('input.txt').split(','))]
    result = {x: [] for x in numbers}
    prev = None
    for idx, key in enumerate(numbers):
        prev = key
        result[key].append(idx)
    for turn in range(len(numbers), iteration):
        value = 0
        if len(result[prev]) > 1:
            value = result[prev][-1] - result[prev][-2]
        result.setdefault(value, []).append(turn)
        prev = value
    print(prev)

def main1():
    main(2020)

def main2():
    main(30000000)
    
if __name__ == "__main__":
    main1()
    main2()
