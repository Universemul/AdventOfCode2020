def read_file(f=None):
    with open('/Users/d.barthelemy/AdventOfCode2020/day2/input.txt', 'r') as f:
        for line in f:
            yield f(line) if f else line
            
