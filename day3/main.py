class ContextFile:

    def __init__(self, lines, step_x=3, step_y=1):
        self.lines = lines
        self.x = 0
        self.y = 0
        self.max_x = len(self.lines[0])
        self.max_y = len(self.lines)
        self.step_x = step_x
        self.step_y = step_y

    def compute_next_coord(self):
        self.x = (self.x + self.step_x) % self.max_x
        self.y = self.y + self.step_y
    
    def can_move(self):
        return self.y < self.max_y

    def is_a_tree(self):
        return self.lines[self.y][self.x] == '#'

def read_file():
    with open('input.txt', 'r') as f:
        data = [line.rstrip() for line in f]
        return data

def count_tree(context: ContextFile):
    tree_count = 0
    while context.can_move():
        if context.is_a_tree():
            tree_count += 1
        context.compute_next_coord()
    return tree_count

def main1():
    context = ContextFile(read_file())
    print(count_tree(context))

def main2():
    tree_count = 1
    for (s_x, s_y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        context = ContextFile(read_file(), s_x, s_y)
        tree_count *= count_tree(context)
    print(tree_count)
    
if __name__ == "__main__":
    main1()
    main2()
