def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def is_safe(i, max_row, j, max_col):
    return 0 <= i < max_row and 0 <= j < max_col

def adjacents(i, j, seats, max_row, max_col):
    result = 0
    for new_i, new_j in [(i + a, j + b) for a in (-1,0,1) for b in (-1,0,1) if a != 0 or b != 0]:
        if is_safe(new_i, max_row, new_j, max_col) and seats[new_i][new_j] == '#':
            result += 1
    return result

def more_adjacents(i, j, seats, max_row, max_col):
    result = 0
    directions = (-1, 0, 1)
    for new_i, new_j in [(a,b) for a in directions for b in directions if a != 0 or b != 0]:
        _a = i + new_i
        _b = j + new_j
        while (is_safe(_a, max_row, _b, max_col) and seats[_a][_b] == '.'):
            _a += new_i
            _b += new_j
        if is_safe(_a, max_row, _b, max_col) and seats[_a][_b] == '#':
            result += 1
    return result

def compute_diff(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

def compute_new_line(row, diff, threshold, i, max_col):
    line = []
    for j in range(max_col):
        t = diff[(i, j)]
        if row[j] == 'L' and t == 0:
            line.append('#')
        elif row[j] == '#' and t >= threshold:
            line.append('L')
        else:
            line.append(row[j])
    return line, compute_diff(line, row) 

def main(part, threshold):
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
                if part == 1:
                    adj = adjacents(i, j, seats, max_row, max_col)
                else:
                    adj = more_adjacents(i, j, seats, max_row, max_col)
                diff[(i, j)] = adj
        new_seats = []
        for i in range(max_row):
            line, changes = compute_new_line(seats[i], diff, threshold, i, max_col)
            new_changes += changes
            new_seats.append(''.join(line))
        seats = [*new_seats]
        if new_changes == 0:
            break
    print(len([1 for line in seats for x in line if x == '#']))

def main1():
    main(1, 4)

def main2():
    main(2, 5)

if __name__ == "__main__":
    main1()
    main2()
