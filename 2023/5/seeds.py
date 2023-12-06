import sys

class Map:

    def __init__(self):
        self._map = {}

    def add(self, source, target, length):
            self._map[source] = (target,length)

    def find(self, source):
        for s, (t,l) in self._map.items():
            if source >= s and source < s+l:
                 return t + (source - s)
        return source


def eval_maps(maps, source):
    for m in maps:
        print("Mapping {} to {}".format(source, m.find(source)))
        source = m.find(source)
    return source

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
    for seed in seeds:
        print(eval_maps(maps, seed))
    print(min(eval_maps(maps, seed) for seed in seeds))