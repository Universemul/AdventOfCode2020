from copy import copy

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def adjacents(i, j, seats, max_row, max_col):
    result = 0
    for new_i, new_j in [(i + a, j + b) for a in (-1,0,1) for b in (-1,0,1) if a != 0 or b != 0]:
        if 0 <= new_i < max_row and 0 <= new_j < max_col and seats[new_i][new_j] == '#':
            result += 1
    return result

def main1():
    seats = [x for x in read_file('input.txt')]
    max_row = len(seats)
    max_col = len(seats[0])
    while True:
        diff = dict()
        new_changes = 0
        for i in range(max_row):
            for j in range(max_col):
                if seats[i][j] == '.':
                    diff[(i, j)] = 0
                    continue
                adj = adjacents(i, j, seats, max_row, max_col)
                diff[(i, j)] = adj
        new_seats = []
        for i in range(max_row):
            line = []
            for j in range(max_col):
                if seats[i][j] == 'L' and diff[(i, j)] == 0:
                    line.append('#')
                elif seats[i][j] == '#' and diff[(i, j)] >= 4:
                    line.append('L')
                else:
                    line.append(seats[i][j])
                if seats[i][j] != line[j]:
                    new_changes += 1
            new_seats.append(''.join(line))
        seats = new_seats
        if new_changes == 0:
            break
    print(len([1 for line in seats for x in line if x == '#']))

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    main2()
