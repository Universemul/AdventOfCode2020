def read_file_by_split(filename):
    return open(filename).read().strip().replace("\n\n", "_").split('_')

class Group:

    def __init__(self, data):
        self.data = set(data.replace("\n", ""))
        self.data_by_person = [set(x) for x in data.split("\n")]
        self.count_questions = 0
        self.question_everyone_answered = 0

    def build(self):
        self.count_questions = len(self.data)
        self.question_everyone_answered = len(set.intersection(*self.data_by_person))
        return self
        
def main1():
    lines = read_file_by_split('input.txt')
    groups = []
    for group in lines:
        groups.append(Group(group).build())
    print(sum([x.count_questions for x in groups]))
    print(sum([x.question_everyone_answered for x in groups]))

if __name__ == "__main__":
    main1()
