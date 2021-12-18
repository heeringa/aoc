import sys


    
class PT:

    def __init__(self, x, y, vx, vy, x1, y1, x2, y2):
        """x1,y1 is BL -- x2,y2 is TR"""
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.maxheight = self.y
        
    def next(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.vx = self.vx + self._sign(self.vx)
        self.vy = self.vy - 1
        self.maxheight = max(self.y, self.maxheight)

    def intersects(self):
        return self.x <= self.x2 and self.x >= self.x1 and self.y >= self.y1 and self.y <= self.y2

    def below(self):
        """x1,y1 is BL -- x2,y2 is TR"""
        return self.y < self.y1

    def right(self):
        return self.x > self.x2

    def _sign(self, x):
        if x > 0:
            return -1
        elif x < 0:
            return 1
        else:
            return 0


if __name__ == '__main__':

    x1 = 201
    y1 = -99
    x2 = 230
    y2 = -65

    maxheight = y1
    count = 0
    # we never need to simulate launches higher than the
    # the magnnitude of the distance below the target
    # area from 0
    for yv in range(y1,-y1+1):
        # we never need to simulate launches to the right of the target area
        for xv in range(1,x2+1):
            p = PT(0,0,xv,yv,x1,y1,x2,y2)
            
            # simulate P
            while not p.below():
                if p.intersects():
                    maxheight = max(maxheight, p.maxheight)
                    count = count + 1
                    break
                p.next()

    print(maxheight)
    print(count)
        


    
