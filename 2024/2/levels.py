import sys


def safe(line):

    def descend(line):
        for i in range(0,len(line)-1):
            diff = line[i] - line[i+1]
            if diff >= 1 and diff <= 3:
                continue
            else:
                return False
        return True
    
    def ascend(line):
        for i in range(0,len(line)-1):
            diff = line[i+1] - line[i]
            if diff >= 1 and diff <= 3:
                continue
            else:
                return False
        return True
    
    if line[0] > line[1]:
        return descend(line)
    else:
        return ascend(line)

def parse(line):
    return [int(x) for x in line.strip().split()]

if __name__ == '__main__':
    count = 0
    with open(sys.argv[1]) as fin:
        for line in fin:
            if safe(parse(line)):
                count += 1
    print(count)