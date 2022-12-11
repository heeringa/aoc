import sys
import re

class Monkey:


    def __init__(self, items, op, divisible, t, f):
        self.items = items
        self.op = op
        self.divisible = divisible
        self.t = t
        self.f = f
        self.count = 0

    def throw(self, worry, monkeys):
        if worry % self.divisible == 0:
            return monkeys[self.t].add(worry)
        else:
            return monkeys[self.f].add(worry)

        
    def iterItems(self):
        while len(self.items) != 0:
            self.count += 1
            yield self.op(self.items.pop(0)) // 3

    def add(self, worry):
        self.items.append(worry)

    def __str__(self):
        return " ".join([str(i) for i in self.items])

def val(x, s):
    if s.strip() == 'old':
        return x
    else:
        return int(s)

def retf(line):

    rhs = line.strip().split(":")
    rhs = rhs[1].strip()
    rhs = rhs.split("=")
    rhs = rhs[1].strip()[4:]
    op = rhs[0].strip()
    
    def fn(x):
        if op == '+':
            return x + val(x, rhs[2:])
        else:
            return x * val(x, rhs[2:])

    return fn
    
def parse(line):

    items = line[1].split(":")
    items = items[1].strip()
    items = [int(item) for item in items.split(',')]


    fn = retf(line[2])


    test_reg = "\s*Test:\s*divisible\s*by\s*(\d+)"
    match = re.search(test_reg, line[3])
    test = int(match.group(1))

    true_reg = "\s*If\s*true:\s*throw\s*to\s*monkey\s*(\d+)"
    match = re.search(true_reg, line[4])
    t = int(match.group(1))

    fals_reg = "\s*If\s*false:\s*throw\s*to\s*monkey\s*(\d+)"
    match = re.search(fals_reg, line[5])
    f = int(match.group(1))    

    return Monkey(items, fn, test, t, f)
    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = []
        monkeys = []
        for line in f:
            if line.strip() == '':
                monkeys.append(parse(lines))
                lines = []
            else:
                lines.append(line)
        monkeys.append(parse(lines))

        rounds = 20
        
        for round in range(rounds):

            for monkey in monkeys:

                for worry in monkey.iterItems():
                    monkey.throw(worry, monkeys)

        
        counts = [monkey.count for monkey in monkeys]
        counts.sort(reverse=True)
        print(counts)
        print(counts[0]*counts[1])
