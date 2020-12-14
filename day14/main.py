def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

class Mask:
    def __init__(self, value):
        self.value0 = int(value.replace('X', '0'), base=2)
        self.value1 = int(value.replace('X', '1'), base=2)

class Instruction:

    def __init__(self, idx, value):
        self.value = int(value)
        self.index = int(idx)

    def compute(self, mask: Mask):
        return (self.value & mask.value1) | mask.value0

def main1():    
    lines = read_file('input.txt')
    _input = list()
    for l in lines:
        operator, value = [x.strip() for x in l.split('=')]
        if operator == 'mask':
            _input.append(Mask(value))
        else:
            idx = operator.replace("mem[", "").replace(']', '')
            _input.append(Instruction(idx, value))
    mask = None
    result = dict()
    for instruction in _input:
        if type(instruction) is Mask:
            mask = instruction
        else:
            result[instruction.index] = instruction.compute(mask)
    print(sum(result.values()))

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    main2()
