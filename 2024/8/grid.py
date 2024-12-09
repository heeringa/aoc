import sys


def locations(grid):
    locs = {}
    w = len(grid[0])
    h = len(grid)
    for j in range(h):
        for i in range(w):
            item = grid[j][i]
            if item != '.':
                locs.setdefault(item,[]).append((i,j))
    return locs
    

def iterpair(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    if x1 < x2:
        x3 = x1-dx
        x4 = x2+dx
    else:
        x3 = x1+dx
        x4 = x2-dx
    if y1 < y2:
        y3 = y1-dy
        y4 = y2+dy
    else:
        y3 = y1+dy
        y4 = y2-dy

    yield x3,y3
    yield x4,y4


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        grid = [list(line.strip()) for line in fin]
        w = len(grid[0])
        h = len(grid)

        locs = locations(grid)
        print(locs)
        points = set()
        for vals in locs.values():
            for i in range(len(vals)):
                for j in range(i+1,len(vals)):
                    for x,y in iterpair(vals[i], vals[j]):
                        if x >= 0 and x < w and y >= 0 and y < h:
                            points.add((x,y))
        print()
        print(points)
        print(len(points))
                

