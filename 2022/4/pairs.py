import sys

class Range:

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def contains(self, other):
        return self.l >= other.l and self.r <= other.r

    @classmethod
    def fromString(cls, s):
        s = s.split('-')
        return cls(int(s[0]), int(s[1]))

    def __str__(self):
        return "{}-{}".format(self.l, self.r)
        
def parse(line):
    pair = line.split(',')
    left = pair[0]
    right = pair[1]
    return Range.fromString(left), Range.fromString(right)
    

def inter(lines):
    total = 0
    for line in lines:
        l,r = parse(line)
        if l.contains(r) or r.contains(l):
            total += 1
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(inter(f))
