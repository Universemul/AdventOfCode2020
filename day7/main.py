import re

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

MY_BAG = "shiny gold"

class Bag:

    def __init__(self, data):
        parsed_data = self.parse(data)
        self.key = parsed_data[0]
        self.bags = parsed_data[1]
        self.bag_names = [x[1] for x in self.bags]
    
    def parse(self, data):
        bags = data.split('contain')
        self.key = bags[0].replace("bags", "").strip()
        contained_bags = list()
        for bag in bags[1].split(','):
            b = re.sub(r"bags?|\.", "", bag).strip().split(' ')
            b_name = " ".join(b[1:])
            if b[0] != "no":
                contained_bags.append((int(b[0].strip()), b_name))
        return self.key, contained_bags

def children(bag, cache):
    return {cache[x] for x in bag.bag_names}

def main1():
    lines = read_file('input.txt')
    cache = dict()
    for l in lines:
        bag = Bag(l)
        cache[bag.key] = bag
    result = 0
    for key, bag in cache.items():
        to_process = children(bag, cache)
        while len(to_process) > 0:
            _b = to_process.pop()
            if _b.key == MY_BAG:
                result += 1
                break
            to_process.update(children(_b, cache))
    print(result)

def main2():
    lines = read_file('input.txt')
    cache = dict()
    for l in lines:
        bag = Bag(l)
        cache[bag.key] = bag
    result = 0
    my_bag = cache[MY_BAG]
    bags = list(my_bag.bags)
    while len(bags) > 0:
        count, bag_name = bags.pop()
        result += count
        _c = children(cache[bag_name], cache)
        for x in cache[bag_name].bags:
            bags.append((count * x[0], x[1]))
    print(result)

if __name__ == "__main__":
    main1()
    main2()
