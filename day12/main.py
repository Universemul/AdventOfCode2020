from enum import Enum

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

COEF = {'N': 1, 'E': 1, 'S': -1, 'W': -1, 'R': 1, 'L': -1}

class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    @staticmethod
    def turn(direction, value, current_direction):
        _v = int(value / 90)
        _d = ['N', 'E', 'S', 'W']
        return _d[(_d.index(current_direction) + (_v * COEF[direction])) % 4]

class Ship:
    DIRECTIONS = ['N', 'S', 'E', 'W']

    def __init__(self, direction):
        self.current_direction = direction
        self.values = {x: 0 for x in ['N', 'E']}
    
    def _get_mapping(self, direction):
        if direction == 'S':
            return 'N'
        if direction == 'W':
            return 'E'
        return direction
    
    def compute_new_value(self, direction, value, current_direction):
        return self.values[direction] + (value * COEF[current_direction])

    def move_forward(self, value):
        new_dir = self._get_mapping(self.current_direction)
        new_v = self.compute_new_value(new_dir, value, self.current_direction)
        self.values[new_dir] = new_v

    def move(self, direction, value):
        if direction == 'F':
            self.move_forward(value)
            return
        _d = self._get_mapping(direction)
        new_v = self.compute_new_value(_d, value, direction)
        self.values[_d] = new_v

    def turn(self, direction, value):
        self.current_direction = Direction.turn(direction, value, self.current_direction)

def main1():
    lines = read_file('input.txt')
    ship = Ship('E')
    idx = 0
    for l in lines:
        operator = l[0]
        number = int(l[1:])
        if operator in ['N', 'S', 'E', 'W', 'F']:
            ship.move(operator, number)
        else:
            ship.turn(operator, number)
    print(abs(ship.values['N']) + abs(ship.values['E']))

def main2():
    lines = read_file('input.txt')
    
if __name__ == "__main__":
    main1()
    #main2()
