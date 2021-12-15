import sys


def step(deriv, rules):
    new = []
    for x,y in zip(deriv, deriv[1:]):
        new.append(x)
        new.append(rules["".join([x,y])])
    new.append(deriv[-1])
    return new

def most(lst):
    counts = {}
    for l in lst:
        counts[l] = counts.get(l,0) + 1
    maxVal = None
    for k,v in counts.items():
        if maxVal is None or v > maxVal:
            maxVal = v
    return maxVal

def least(lst):
    counts = {}
    for l in lst:
        counts[l] = counts.get(l,0) + 1
    minVal = None
    for k,v in counts.items():
        if minVal is None or v < minVal:
            minVal = v
    return minVal


if __name__ == '__main__':
    rules = {}
    deriv = list(sys.stdin.readline().strip())
    sys.stdin.readline()
    for line in sys.stdin:
        pairs = line.strip().split('->')
        rules[pairs[0].strip()] = pairs[1].strip()

    STEPS = 10
#    print(rules)
#    print("".join(deriv))
    for _ in range(STEPS):
        deriv = step(deriv,rules)
#        print("".join(deriv))

    m1 = most(deriv)
    m2 = least(deriv)

    print(m1)
    print(m2)
    print(m1-m2)
    
            
