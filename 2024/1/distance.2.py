import sys


def parse(lines):
    left = []
    counts = {}
    for line in lines:
        pair = line.strip().split()
        left.append(int(pair[0]))
        right = int(pair[1])
        counts[right] = counts.get(right,0) + 1
    return (left, counts)

def distance(left, counts):
    total = 0
    for l in left:
        total += l*counts.get(l,0)
    return total


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        lines = fin.readlines()
    left, counts = parse(lines)
    print(distance(left,counts))