from enum import Enum

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

    @staticmethod
    def turn(direction, value, current_direction):
        _v = int(value / 90)
        _d = ['N', 'E', 'S', 'W']
        return _d[(_d.index(current_direction) + (_v * COEF[direction])) % 4]

class Ship:
    
    CARDINALS = {'N': (0, 1), 'S': (0, -1), 'E': (1, 1), 'W': (1, -1)}
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.direction = 'E'
        self.values = [0, 0] # North, East
    
    def _get_mapping(self, direction):
        return self.CARDINALS[direction]

    def compute_new_value(self, direction, value):
        idx, coef = self._get_mapping(direction)
        self.values[idx] += (value * coef)

    def move(self, direction, value):
        _direction = direction
        if direction == 'F':
            _direction = self.direction
        self.compute_new_value(_direction, value)

    def turn(self, direction, value):
        coef = -1 if direction == 'L' else 1
        _v = int(value / 90) * coef
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + _v) % 4]

def main1():
    lines = read_file('input.txt')
    ship = Ship()
    for l in lines:
        operator = l[0]
        number = int(l[1:])
        if operator in ['N', 'S', 'E', 'W', 'F']:
            ship.move(operator, number)
        else:
            ship.turn(operator, number)
    print(abs(ship.values[0]) + abs(ship.values[1]))

"""
-------- PART 2 --------
"""

def turn_waypoint(waypoint, operator, value):
    clockwise = value
    if operator == 'L':
        clockwise = 360 - value
    waypoint = {
        90: [-waypoint[1], waypoint[0]],
        180: [-waypoint[0], -waypoint[1]],
        270: [waypoint[1], -waypoint[0]]
    }[clockwise]
    return waypoint

def move_ship(waypoint, ship, value):
    ship[0] = ship[0] + (value * waypoint[0])
    ship[1] = ship[1] + (value * waypoint[1])
    return ship

def move_waypoint(waypoint, operator, value):
    coef, position = {
        'N': (1, 0), # coef,position in waypoint
        'S': (-1, 0),
        'E': (1, 1),
        'W': (-1, 1)
    }[operator]
    waypoint[position] += value * coef
    return waypoint

def main2():
    lines = read_file('input.txt')
    waypoint = [1, 10] # (North/Sud East/West
    ship = [0, 0]
    for l in lines:
        operator = l[0]
        number = int(l[1:])
        if operator == "F":
            ship = move_ship(waypoint, ship, number)
        elif operator in ['N', 'S', 'E', 'W']:
            waypoint = move_waypoint(waypoint, operator, number)
        else:
            waypoint = turn_waypoint(waypoint, operator, number)
    print(abs(ship[0]) + abs(ship[1]))

if __name__ == "__main__":
    main1()
    main2()
