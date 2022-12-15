import sys
import re
from copy import copy

class RangeSet:

    def __init__(self, ranges):
        self.ranges = self.union(ranges)

    def __str__(self):
        return " ".join([str(r) for r in self.ranges])
        
    def union(self, ranges):
        rngs = copy(ranges)
        other = []
        while len(rngs) != 0:
            r = rngs.pop()
            over = False
            for i in range(len(rngs)):
                if rngs[i].overlap(r):
                    rngs[i] = rngs[i].union(r)
                    over = True
                    break;
            if not over:
                other.append(r)
        return other

    def length(self, beacons):
        length = 0
        for r in self.ranges:
            length += r.length()
            for b in beacons:
                if r.contains(b):
                    print("Range {} contains beacon {}".format(r,b))
                    length -= 1
        return length
    
class Range:


    def __init__(self, r):
        p1, p2 = r
        self.left = p1[0]
        self.right = p2[0]
        self.y = p1[1]


    def contains(self, x):
        return self.left <= x and self.right >= x
    
    def length(self):
        return self.right-self.left+1
    
    def __copy__(self):
        return Range((self.left,y),(self.right,y))

    def __str__(self):
        return "Y={} ({},{})".format(self.y, self.left, self.right)
    
    def overlap(self, other):
        if other.y == self.y:
            return other.left <= self.right and other.right >= self.left
        else:
            return False

    def union(self, other):
        if self.overlap(other):
            l = min(other.left,self.left)
            r = max(other.right,self.right)
            return Range(((l,self.y),(r,self.y)))
        else:
            return None
        

class PointSet:

    def __init__(self, x, y, maxdist):
        self.x = x        
        self.y = y
        self.maxdist = maxdist


    def rangeat(self, y2):
        dx = abs(self.y - y2)
        if dx > self.maxdist:
            return None
        else:
            return ((self.x-(self.maxdist-dx), y2),(self.x+(self.maxdist-dx),y2))

    def __str__(self):
        ranges = []
        for y2 in range(self.maxdist+1):
            ranges.append(self.rangeat(self.y + y2))
            ranges.append(self.rangeat(self.y - y2))
                    
        return "({},{}) maxdist: {}\n{}".format(self.x, self.y, self.maxdist, "\n".join([str(r) for r in ranges]) + "\n")
            
        
if __name__ == '__main__':

    regex = "\s*Sensor\s*at\s*x=(-?\d+),\s*y=(-?\d+):\s*closest\s*beacon\s*is\s*at\s*x=(-?\d+),\s*y=(-?\d+)\s*"
    with open(sys.argv[1]) as f:
        sets = []
        beacons = set()
        i = 0
        for line in f:
            match = re.search(regex, line)
            x1 = int(match.group(1))
            y1 = int(match.group(2))
            x2 = int(match.group(3))
            y2 = int(match.group(4))
            dx = abs(x1-x2)
            dy = abs(y1-y2)
            S = PointSet(x1, y1, dx+dy)
            beacons.add((x2,y2))
            sets.append(S)

        Y = 2000000
        beacons = [x for (x,y) in list(beacons) if y == Y]
        ranges = [Range(p.rangeat(Y)) for p in sets if p.rangeat(Y) is not None]
         
        for r in ranges:
            print(r)

        print()
        R = RangeSet(ranges)

        print(R)

        print(beacons)
        print(R.length(beacons))
             
#        F = set()
#        for s in sets:
#            print(s)
#            print(list(s))
#            for p in list(s):
#                print(p)
#                if p[1] == 10:
#                    F.add(p)
#        print(sorted(list(F)))
#        print(len(F))
#        print(F-beacons)
#        print(len(F-beacons))
            

    
