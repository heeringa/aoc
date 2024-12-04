import sys
import re


def findlines(s):
    start = 0
    total = 0
    pattern = "don't()"
    end = s.find(pattern, start)
    while end != -1:
        total += compute(s[start:end])
        start = s.find("do()", end+len(pattern))
        if start != -1:
            end = s.find(pattern, start+len("do()"))
            if end == -1:
                total += compute(s[start:])
        else:
            end = -1
    return total
            

def compute(line):
    regex = "mul\((\d+),(\d+)\)"
    total = 0
    for mtch in re.finditer(regex, line):
        prod = 1
        for p in mtch.groups():
            prod *= int(p)
        total += prod
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        lines = fin.read()
        print(findlines(lines))


        