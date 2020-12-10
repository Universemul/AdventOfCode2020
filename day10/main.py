def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def get_diff(rating, target, data, differences):
    sources = [rating + i for i in range(1, 4)]
    for x in sources:
        if x in data:
            diff = x - rating
            rating = x
            if rating + 3 == target:
                differences.setdefault(3, 0)
                differences[3] += 1
            differences.setdefault(diff, 0)
            differences[diff] += 1
            data.remove(rating)
            get_diff(rating, target, data, differences)

def main1():
    lines = list(read_file('input.txt', int))
    target = max(lines) + 3
    differences = dict()
    get_diff(0, target, lines, differences)
    print(differences)
    print(differences.get(1, 1) * differences.get(3, 1))

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    main2()

