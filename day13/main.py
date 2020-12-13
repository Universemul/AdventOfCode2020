import math

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def main1():
    lines = list(read_file('input.txt'))
    my_time = int(lines[0])
    bus_ids = {int(x): math.ceil(my_time/int(x)) for x in lines[1].split(',') if x != 'x'}
    matrix = [(key, val * key) for key, val in bus_ids.items()]
    time = min([x[1] for x in matrix])
    bus_id = next(x[0] for x in matrix if x[1] == time)
    print((time - my_time) * bus_id)

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    main2()
