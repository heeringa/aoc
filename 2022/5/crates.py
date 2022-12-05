import sys
import re

def itercrate(line):
    crate = None
    print("Current Crate Line = {}".format(line))
    if line != '':
        crate = line[0:4]
        crate = crate.strip()
        print("Parse {} from line".format(crate))
        yield crate
        print("Continuing with {}".format(line[4:]))
        yield from itercrate(line[4:])


def parsecrates(input, len):

    print(len)
    print(input)
    
    crates = [[] for _ in range(len)]
    
    for line in input:
        for crate,l in zip(itercrate(line),crates):
            if crate != '':
                l.append(crate[1])

    for crate in crates:
        crate.reverse()

    return crates
            
        

def solve(input):
    crateinput = []
    directions = []
    dirstate = False
    for line in input:
        if line == '\n':
            dirstate = True
        elif dirstate:
            directions.append(line)
        else:
            crateinput.append(line)

    nums = crateinput.pop().strip()
    crates = parsecrates(crateinput, int(nums[-1]))

    regex = "\s*move\s*(\d+)\s*from\s*(\d+)\s*to\s*(\d+)\s*"

    print(crates)
    
    for line in directions:
        result = re.search(regex,line)
        moves = int(result.group(1))
        fromstack = int(result.group(2))
        tostack = int(result.group(3))
        for _ in range(moves):
            crates[tostack-1].append(crates[fromstack-1].pop())

    s = ''.join([crate.pop() for crate in crates])
    print(s)
    


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        solve(f)

    
