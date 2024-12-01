import sys


def parse(lines):
    left = []
    right = []
    for line in lines:
        pair = line.strip().split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))
    return (sorted(left), sorted(right))

def distance(left, right):
    total = 0
    for l,r in zip(left,right):
        total += abs(l-r)
    return total


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        lines = fin.readlines()
    left, right = parse(lines)
    print(distance(left,right))