import sys


def step(pair_cnts, totals, rules):
    new_cnts = {}
    new_totals = totals.copy()
    for pair, cnt in pair_cnts.items():
        x,y = pair[0], pair[1]
        z = rules["".join(pair)]
        xz = "".join([x,z])
        pair_cnt = pair_cnts.get(pair,0)
        new_cnts[xz] = new_cnts.get(xz,0) + pair_cnt
        zy = "".join([z,y])
        new_cnts[zy] = new_cnts.get(zy,0) + pair_cnt
        new_totals[z] = new_totals.get(z,0) + pair_cnt        
    return new_cnts, new_totals

def most(counts):
    maxVal = None
    for k,v in counts.items():
        if maxVal is None or v > maxVal:
            maxVal = v
    return maxVal

def least(counts):
    minVal = None
    for k,v in counts.items():
        if minVal is None or v < minVal:
            minVal = v
    return minVal


if __name__ == '__main__':
    rules = {}
    st = list(sys.stdin.readline().strip())
    pair_counts = {}
    for x,y in zip(st,st[1:]):
        z = "".join([x,y])
        pair_counts[z] = pair_counts.get(z,0) + 1
    totals = {}
    for s in st:
        totals[s] = totals.get(s,0) + 1
        
    sys.stdin.readline()
    for line in sys.stdin:
        pairs = line.strip().split('->')
        rules[pairs[0].strip()] = pairs[1].strip()

    STEPS = 40
    print(rules)
    print(pair_counts)
    print(totals)
    for i in range(STEPS):
        pair_counts, totals = step(pair_counts,totals,rules)
        print("Afer step {}".format(i+1))
        print("Pair Counts = {}".format(pair_counts))
        print("Totals = {}".format(totals))
        print()

    m1 = most(totals)
    m2 = least(totals)

    print(m1)
    print(m2)
    print(m1-m2)
    
            
