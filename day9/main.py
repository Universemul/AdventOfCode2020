def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

PREAMBLE = 25

def main1():
    lines = list(read_file('input.txt', lambda x: int(x)))
    data = lines[PREAMBLE:]
    for idx, number in enumerate(data):
        base = lines[idx:idx+PREAMBLE]
        tmp = [number - x for x in base]
        if not any(x for x in tmp if x in base):
            print(number)
            break


def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    main2()
