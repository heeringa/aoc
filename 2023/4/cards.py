import sys
import re

def parse(line):
    r = "Card\s+\d+:\s+(.*)"
    pairs = re.findall(r,line)[0].split('|')
    return ([int(i) for i in pairs[0].split()], 
            [int(i) for i in pairs[1].split()])

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        total = 0
        for line in f:
            wins, nums = parse(line)
            l = len(set(wins).intersection(set(nums)))
            if l > 0:
                total += 2**(l-1)
        print(total)
