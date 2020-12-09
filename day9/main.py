def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

PREAMBLE = 25

def get_lines():
    return list(read_file('input.txt', lambda x: int(x)))

def main1(lines):
    data = lines[PREAMBLE:]
    for idx, number in enumerate(data):
        base = lines[idx:idx+PREAMBLE]
        tmp = [number - x for x in base]
        if not any(x for x in tmp if x in base):
            return number


def main2(lines):
    number = main1(lines)
    idx = 0
    while idx < len(lines):
        numbers = []
        j = idx
        while (sum(numbers) < number):
            numbers.append(lines[j])
            j += 1
        idx += 1
        if sum(numbers) == number:
            print(min(numbers) + max(numbers))
            return

if __name__ == "__main__":
    lines = get_lines()
    print(main1(lines))
    main2(lines)
