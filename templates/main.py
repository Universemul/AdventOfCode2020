def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

def main1():
    lines = read_file('input.txt')

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    main2()
