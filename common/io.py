def read_file(filename, f=None):
    with open(filename, 'r') as f:
        for line in f:
            yield f(line) if f else line
            
