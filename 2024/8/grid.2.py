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
    

def iterpair(p1,p2,w,h):
    pairs = []
    x1,y1 = p1
    x2,y2 = p2
    
    # we'll always assume x1 is leftmost point
    if x1 > x2:
        x1,y1 = p2
        x2,y2 = p1

    dx = abs(x2-x1)
    dy = abs(y2-y1)
    if y1 < y2:        
        # TOPLEFT / BOTTOM RIGHT
        x3 = x1-dx            
        y3 = y1-dy              
        while x3 >= 0 and y3 >= 0:
            pairs.append((x3,y3))
            x3 = x3-dx
            y3 = y3-dy
        x4 = x2+dx            
        y4 = y2+dy            
        while x4 < w and y4 < h:
            pairs.append((x4,y4))
            x4 = x4+dx
            y4 = y4+dy
            
    else:
        # BOTTOM LEFT / TOP RIGHT
        x3 = x1-dx            
        y3 = y1+dy              
        while x3 >= 0 and y3 < h:
            pairs.append((x3,y3))
            x3 = x3-dx
            y3 = y3+dy
        x4 = x2+dx            
        y4 = y2-dy            
        while x4 < w and y4 >= 0:
            pairs.append((x4,y4))
            x4 = x4+dx
            y4 = y4-dy

    for x,y in pairs:
        yield (x,y)


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        grid = [list(line.strip()) for line in fin]
        w = len(grid[0])
        h = len(grid)

        locs = locations(grid)
        print(locs)
        points = set()
        for vals in locs.values():
            for x,y in vals:
                points.add((x,y))
            for i in range(len(vals)):
                for j in range(i+1,len(vals)):
                    for x,y in iterpair(vals[i], vals[j], w, h):
                        points.add((x,y))
        
        for (x,y) in points:
            grid[y][x] = '#'
        
        print('\n'.join([''.join(line) for line in grid]))
        
        print()
        print(points)
        print(len(points))
                

