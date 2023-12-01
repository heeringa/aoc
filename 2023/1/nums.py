import sys

def parse_line(line):
    first = None
    last = None
    for c in line:
        try:
            first = int(c)
            break
        except ValueError:
            continue
    for c in reversed(line):
        try:
            last = int(c)
            break
        except ValueError:
            continue
    return first*10 + last

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        total = 0
        for line in f:
            total += parse_line(line)
        print(total)
