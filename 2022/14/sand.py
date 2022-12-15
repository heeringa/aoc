import sys

def addpoints(x1, y1, x2, y2, points):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    if dx == 0:
        m = min(y1,y2)
        for i in range(dy+1):
            points.add((x1,m+i))
    if dy == 0:
        m = min(x1,x2)
        for i in range(dx+1):
            points.add((m+i,y1))
            

def parsepoint(p):
    x,y  = p.split(',')
    return (int(x),int(y))


    
class Simulate:

    def __init__(self, rocks):
        self.rocks = rocks
        self.sand = set()
        self.maxy = max([p[1] for p in list(self.rocks)])
        
    def next(self, x, y):
        down = (x,y+1) in self.rocks or (x,y+1) in self.sand
        left = (x-1,y+1) in self.rocks or (x-1,y+1) in self.sand
        right = (x+1,y+1) in self.rocks or (x+1,y+1) in self.sand

        if not down:
            return (True, (x,y+1))
        elif not left:
            return (True, (x-1,y+1))
        elif not right:
            return (True, (x+1,y+1))
        else:
            return (False, (x,y))


    def drop(self):
        x,y = 500,0
        cont, (x,y) = self.next(x,y)
        while (cont):
            cont, (x,y) = self.next(x,y)
            if y > self.maxy:
                return False
        self.sand.add((x,y))
        return True

    def __str__(self):
        xs = [p[0] for p in list(self.rocks)]
        ys = [p[1] for p in list(self.rocks)]
        minx = min(xs)-1
        maxx = max(xs)
        miny = min(min(ys),0)
        maxy = max(ys)
        dx = maxx - minx
        dy = maxy - miny
        pts = [['.']*(dx+3) for _ in range(dy+1)]
        for x,y in self.rocks:
            pts[y-miny][x-minx] = '#'
        for x,y in self.sand:
            pts[y-miny][x-minx] = 'o'
        return "\n".join(["".join(line) for line in pts])
            
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        points = set()
        for line in f:
            pts = line.split(' -> ')
            for p1, p2 in zip(pts, pts[1:]):
                x1,y1 = parsepoint(p1)
                x2,y2 = parsepoint(p2)
                addpoints(x1,y1,x2,y2,points)

        s = Simulate(points)
        i = 0
        while s.drop():
            print(s)
            print()
            i += 1
        print(i)
        
        
                
            
