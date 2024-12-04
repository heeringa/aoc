import sys


def safe(line):

    def descend(line, prv, nxt, tolerate=True):
        if nxt < len(line):
            diff = line[prv] - line[nxt]
            if diff >= 1 and diff <= 3:
                return descend(line, nxt, nxt+1, tolerate)
            else:
                if tolerate:
                    if prv == 0:
                        return descend(line, prv, nxt+1, False) or descend(line, nxt, nxt+1, False)
                    else:
                        return descend(line, prv, nxt+1, False) or descend(line, prv-1, nxt, False)
                else:
                    return False
        return True

    def ascend(line, prv, nxt, tolerate=True):
        if nxt < len(line):
            diff = line[nxt] - line[prv]
            if diff >= 1 and diff <= 3:
                return ascend(line, nxt, nxt+1, tolerate)
            else:
                if tolerate:
                    if prv == 0:
                        return ascend(line, prv, nxt+1, False) or ascend(line, nxt, nxt+1, False)
                    else:
                        return ascend(line, prv, nxt+1, False) or ascend(line, prv-1, nxt, False)
                else:
                    return False
        return True

    return ascend(line, 0, 1, True) or descend(line, 0, 1, True)

def parse(line):
    return [int(x) for x in line.strip().split()]

if __name__ == '__main__':
    count = 0
    with open(sys.argv[1]) as fin:
        for line in fin:
            if safe(parse(line)):
                count += 1
    print(count)