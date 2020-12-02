import re

class PasswordParser:

    def __init__(self, min_: int, max_: int, letter: str, password: str):
        self.min_ = min_
        self.max_ = max_
        self.letter = letter
        self.password = password

    def is_valid(self):
        nbr = self.password.count(self.letter)
        return self.min_ <= nbr <= self.max_
    

# Pattern is min-max caractere: password
def parse_line(line: str):
    pattern = r"(\d+)\-(\d+)\s+(\w){1}:\s+(\w+)"
    matches = re.findall(pattern, line, re.MULTILINE)[0]
    return PasswordParser(int(matches[0]), int(matches[1]), matches[2], matches[3])

def read_file():
    with open('/Users/d.barthelemy/AdventOfCode2020/day2/input.txt', 'r') as f:
        for line in f:
            yield parse_line(line)

def main1():
    lines = read_file()
    count = sum(1 for x in lines if x.is_valid())
    print(f"{count} passwords are valid")

if __name__ == "__main__":
    main1()