import sys
import math

def sgn(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


class Rope:

    def __init__(self, size):
        self.size = size
        self.xs = [0 for _ in range(size)]
        self.ys = [0 for _ in range(size)]
        self.visited = set()
        
    def move(self, direction):
        if direction == "U":
            self.up()
        elif direction == "D":
            self.down()
        elif direction == "R":
            self.right()
        else:
            self.left()

    def __str__(self):
        locs = []
        for i in range(self.size):
            locs.append("{}:({},{})".format(i,self.xs[i],self.ys[i]))
        return " ".join(locs)
    
    def moveTimes(self, direction, times):
        print("Moving {}, {} times".format(direction,times))
        for _ in range(times):
            self.move(direction)
            print(self)
            
    def up(self):
        self.ys[0] += 1
        self.resolve()

    def down(self):
        self.ys[0] += -1
        self.resolve()

    def left(self):
        self.xs[0] += -1
        self.resolve()

    def right(self):
        self.xs[0] += 1
        self.resolve()

    def resolve(self):
        for i in range(1,self.size):
            dx = self.xs[i-1] - self.xs[i]
            dy = self.ys[i-1] - self.ys[i]
            diag = abs(dx) + abs(dy) == 3
            
            if abs(dx) > 1 or diag:
                self.xs[i] += 1*sgn(dx)
            if abs(dy) > 1 or diag:
                self.ys[i] += 1*sgn(dy)

        self.visited.add((self.xs[self.size-1],self.ys[self.size-1]))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        r = Rope(10)
        for line in f:
            direction,num = line.split()
            num = int(num.strip())
            r.moveTimes(direction,num)
        print(r.visited)
        print(len(r.visited))
