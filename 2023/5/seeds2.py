import sys

class Map:

    def __init__(self):
        self._map = {}

    def add(self, source, target, length):
            self._map[source] = (target,length)

    def __str__(self):
        ranges = sorted([(s,(t,l)) for s, (t,l) in self._map.items()])
        ranges = ["[{} {}) -> [{} {})".format(s,s+l,t,t+l) for s,(t,l) in ranges]
        return "\n".join(ranges)

    def collapse(self, m):

        def src(p):
            for s, (t, l) in self._map.items():
                if p >= t and p < t+l:
                    return s + (p - t)
            return p
        
        pts = set()
        for s, (t, l) in m._map.items():
            pts.add(s)
            pts.add(s+l)
        for s,(t,l) in self._map.items():
            pts.add(t)
            pts.add(t+l)
        pts = sorted(pts)
                    
        newmap = Map()
        for i in range(len(pts)-1):
            preimage = src(pts[i])
            newmap.add(preimage, m.find(pts[i]), pts[i+1]-pts[i])
        
        return newmap
    
    def find(self, source):
        for s, (t,l) in self._map.items():
            if source >= s and source < s+l:
                 return t + (source - s)
        return source

    def low_interset(self, start, length):
        pts = set([s for s, (t, l) in self._map.items() if s >= start and s < start+length])
        pts.add(start)
        pts = sorted(pts)
        return min(self.find(p) for p in pts)

if __name__ == '__main__':
    seeds = None
    maps = []
    map = None
    with open(sys.argv[1]) as f:
        for line in f:
            if line.startswith("seeds:"):
                seeds = [int(i) for i in line[len("seeds: ")-1:].split()]
                print("Found Seeds = {}".format(seeds))
            elif line.startswith("\n"):
                if map is not None:
                    maps.append(map)
                map = Map()
                print("Found Blank Line -- starting new Map\n")
            elif line.endswith("map:\n"):
                print("Found Map Header: {}".format(line.strip()))
                pass
            else:
                t, s, l = (int(i) for i in line.split())
                map.add(s, t, l)
                print("Found Map Entry: {} {} {}".format(s, t, l))
        maps.append(map)

    m = maps[0]
    for m2 in maps[1:]:
        m = m.collapse(m2)

    low = None
    for i in range(len(seeds) // 2):
        start, length = seeds[i*2], seeds[i*2+1]
        loc = m.low_interset(start, length)
        if low is None or loc < low:
            low = loc

    print(low)
    
