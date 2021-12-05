import sys

def parse(line):
    s1,s2 = line.split('->')
    return s1.strip().split(','), s2.strip().split(',')

class Line:

    def __init__(self, pt1, pt2):
        self.x1, self.y1 = int(pt1[0]), int(pt1[1])
        self.x2, self.y2 = int(pt2[0]), int(pt2[1])

    def __iter__(self):
        if self.x1 == self.x2:
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2)+1):
                yield (self.x1,y)
        else:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2)+1):
                yield(x,self.y1)
                                                      
    def diag(self):
        return not (self.x1 == self.x2 or self.y1 == self.y2)
    
    def __str__(self):
        return "({},{}) -> ({},{})".format(self.x1, self.y1, self.x2, self.y2)
                
def main():

    pts = {}
    for line in sys.stdin:
        l = Line(*parse(line))
        if not l.diag():
            for pt in l:
                pts[pt] = pts.get(pt,0) + 1

    total = 0
    for pt,cnt in pts.items():
        if cnt > 1:
            total = total + 1
    print(total)

if __name__ == '__main__':
    main()
