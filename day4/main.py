import re

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

class Tag:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def _check_height(self, value):
        mesure = value[-2:]
        if mesure not in ['cm', 'in']:
            return False
        _min, _max = 59, 76
        if mesure == 'cm':
            _min, _max = 150, 193
        return _min <= int(value.replace(mesure, '')) <= _max

    def _check_hair_color(self, value):
        return value[0] == '#' and re.fullmatch(r'#[0-9a-f]{6}', value)

    def is_valid(self):
        return { 
            "cid": lambda x: True,
            "byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
            "eyr": lambda x: 2020 <= int(x) <= 2030,
            "hgt": lambda x: self._check_height(x),
            "hcl": lambda x: self._check_hair_color(x),
            "ecl": lambda x: x in "amb blu brn gry grn hzl oth".split(' '),
            "pid": lambda x: re.fullmatch(r"[0-9]{9}", x)
        }[self.key](self.value)

class Passport:

    VALID_TAG =set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'])
    IGNORE_TAGS = ['cid']

    def __init__(self, tags, version=1):
        self.tags = tags
        self.version = version

    def has_valid_tags(self):
        return all(x.is_valid() for x in self.tags)

    def is_valid(self):
        keys = set(x.key for x in self.tags)
        if not (len(keys) == 8 or (len(keys) == 7 and "cid" not in keys)):
            return False
        if self.version == 2:
            return self.has_valid_tags()
        return True

def main(version):
    lines = read_file('input.txt')
    passports = []
    tags = []
    for l in lines:
        if len(l) == 0:
            passports.append(Passport(tags, version=version))
            tags = []
            continue
        for x in l.split(' '):
            key, value = x.split(':')
            tags.append(Tag(key, value))
    if tags:
        passports.append(Passport(tags))
    print(len([1 for x in passports if x.is_valid()]))

if __name__ == "__main__":
    main(version=1)
    main(version=2)
