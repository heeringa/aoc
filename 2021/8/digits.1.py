import sys


def parse(line):
    first,last = line.split('|')
    first = first.strip().split()
    last = last.strip().split()
    return (first, last)

if __name__ == '__main__':
    total = 0
    digits = [2,3,4,7]
    for line in sys.stdin:
        first, last = parse(line)
#        print("TOTAL = {} LAST = {}".format(total,last))
        for digit in last:
            if len(digit) in digits:
                total = total + 1
    print(total)
