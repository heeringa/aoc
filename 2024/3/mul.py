import sys
import re


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        lines = fin.read()
        print(lines)
        regex = "mul\((\d+),(\d+)\)"
        total = 0
        for mtch in re.finditer(regex, lines):
            prod = 1
            for p in mtch.groups():
                prod *= int(p)
            total += prod
        print(total)
        