import re

def read_file(filename, func=None):
    with open(filename, 'r') as f:
        for line in f:
            yield func(line.strip()) if func else line.strip()

# Match everything inside () that contains only numbers, space or + - * /
PATTERN = re.compile(r"\(([0-9\s\*\+\-\/]+)\)")

# Match if there is addition
ADDITION = re.compile(r"(\d+\s*\+\s*\d+)")

def find_expression_between_parenthesis(line: str, is_part_2: bool):
    matches = PATTERN.search(line)
    while matches:
        line = line.replace(matches.group(0), str(evaluate(matches.group(1), is_part_2)))
        matches = PATTERN.search(line)
    return line

def do_operation(operator, x, y):
    return {
        '+': x + y,
        '*': x * y,
        '-': x - y,
        '/': x / y
    }[operator]

def evaluate_plus_first(exp):
    matches = ADDITION.search(exp)
    while matches:
        values = [int(x.strip()) for x in matches.group(0).split('+')]
        exp = exp.replace(matches.group(0), str(do_operation('+', values[0], values[1])), 1)
        matches = ADDITION.search(exp)
    return exp

def evaluate(exp, is_part_2: bool):
    if is_part_2:
        exp = evaluate_plus_first(exp)
    values = [x for x in exp.split(' ')]
    v = int(values[0])
    i = 1
    while i < len(values):
        operator = values[i]
        v = do_operation(operator, v, int(values[i + 1]))
        i += 2
    return v
         
def main(is_part_2=False):
    lines = read_file('input.txt')
    result = 0
    for l in lines:
        exp = find_expression_between_parenthesis(l, is_part_2)
        result += evaluate(exp, is_part_2)
    print(result)

def main1():
    main()

def main2():
    main(True)

if __name__ == "__main__":
    main1()
    main2()
