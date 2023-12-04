import sys
import re

def parse(line):
    r = "Card\s+\d+:\s+(.*)"
    pairs = re.findall(r,line)[0].split('|')
    return ([int(i) for i in pairs[0].split()], 
            [int(i) for i in pairs[1].split()])

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        scores = []
        lines = [line for line in f][::-1]
        for line in lines:
            wins, nums = parse(line)
            l = len(set(wins).intersection(set(nums)))
            if l == 0:
                scores.append(1)
            else:
                L = len(scores)
                scores.append(1+sum(scores[L-l:]))
        print(sum(scores))
