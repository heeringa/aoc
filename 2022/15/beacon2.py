import sys
import re
from copy import copy

class RangeSet:

    def __init__(self, ranges):
        self.ranges = self.union(ranges)

    def __str__(self):
        return " ".join([str(r) for r in self.ranges])

    
    def diff(self, left, right, y):

        l = left
        r = right
        rngs = []
        for r in self.ranges:
            if l < r.left:
                rngs.append(Range(((l,y),(r.left-1,y))))
            l = r.right+1
            if (l > right):
                break
        if l <= right:
            rngs.append(Range(((l,y),(right,y))))

        return RangeSet(rngs)
            
        
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
        other.sort()
        return other


    def length(self, beacons):
        length = 0
        for r in self.ranges:
            length += r.length()
            for b in beacons:
                if r.contains(b):
                    length -= 1
        return length
    
class Range:
    
    def __init__(self, r):
        p1, p2 = r
        self.left = p1[0]
        self.right = p2[0]
        self.y = p1[1]

    def __lt__(self, other):
        return self.left < other.left

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.right > other.right
        
    def contains(self, r):
        return self.left <= r.left and self.right >= r.right
    
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

        X=4000000
        Y=4000000
        for y in range(Y+1):
            rs = RangeSet([Range(p.rangeat(y)) for p in sets if p.rangeat(y) is not None])
            r = rs.diff(0,Y,y)
            if len(r.ranges) != 0:
                x = r.ranges[0].left
                print(x*X+y)

             
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
            

    
