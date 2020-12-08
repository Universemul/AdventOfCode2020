import re

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

class Interpretor:

    def __init__(self, lines):
        self.accumulator = 0
        self.visited_line_index = set()
        self.lines = list(lines)
        self.index = 0
        self.func = {
            "acc": self.add,
            "jmp": self.jump,
            "nop": self.nop
        }

    def add(self, value):
        self.accumulator += value
        self.index += 1

    def jump(self, value):
        self.index += value

    def nop(self, value):
        self.index += 1

    def parse_line(self):
        line = self.lines[self.index]
        instruction, value = line.split(' ')
        value = int(value)
        self.func[instruction](value)

    def start(self):
        self._compute()

    def _compute(self):
        if self.index in self.visited_line_index:
            return
        self.visited_line_index.add(self.index)
        self.parse_line()
        if self.index < len(self.lines):
            self._compute()

def main1():
    lines = read_file('input.txt')
    ip = Interpretor(lines)
    ip.start()
    print(ip.accumulator)

def main2():
    lines = list(read_file('input.txt'))
    _len = len(lines)
    for i in range(_len):
        if not lines[i].startswith('jmp') and not lines[i].startswith('nop'):
            continue
        _lines = list(lines)
        instruction = _lines[i][:3]
        _lines[i] = _lines[i].replace(instruction, "nop" if instruction == "jmp" else "jmp")
        ip = Interpretor(_lines)
        ip.start()
        if ip.index == _len:
            print(ip.accumulator)
    
if __name__ == "__main__":
    main1()
    main2()
