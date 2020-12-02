def read_file():
    with open('input.txt', 'r') as f:
        data = [int(line.rstrip()) for line in f]
        return data

def main_1():
    data = read_file()
    for x in data:
        if 2020 - x in data:
            return (x * (2020 - x))
    return None

def main_2():
    data = read_file()
    s_data = set(data)
    len_ = len(data) - 1
    for idx, elem in enumerate(data):
        if idx == len_:
            break
        j = 0
        while j <= len_:
            if j == idx or j + 1 > len_:
                j += 1
                continue
            next_ = data[j + 1]
            p_sum = elem + next_
            if 2020 - p_sum in s_data:
                return elem * next_ * (2020 - p_sum)
            j += 1
    return None

if __name__ == "__main__":
    number = main_1()
    print(number)

    number = main_2()
    print(number)