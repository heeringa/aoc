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
    
    rm = None
    sf = descend(line) or ascend(line)
    if sf:
        return True, None
    if not sf:
        for i in range(0,len(line)):
            l = line[:i] + line[i+1:]
            sf = descend(l) or ascend(l)
            rm = line[i]
            if sf:
                return sf, rm
    return False, None
 

def parse(line):
    return [int(x) for x in line.strip().split()]

if __name__ == '__main__':
    count = 0
    with open(sys.argv[1]) as fin:
        for line in fin:
            val, rm = safe(parse(line))
            print("{} :: {} {}".format(line.strip() , val, rm))
            if val:
                count += 1
    print(count)