import sys, math



class Pair:

    def __init__(self, left, right, depth=0, parent=None):
        self.depth = depth
        self.left = left
        self.right = right

        if not isinstance(self.left, int):
            self.left.increasedepth()
            self.left.parent = self
        if not isinstance(self.right, int):
            self.right.parent = self
            self.right.increasedepth()
            
        self.parent = parent
        

    def increasedepth(self):
        self.depth += 1
        if not isinstance(self.left, int):
            self.left.increasedepth()
        if not isinstance(self.right, int):
            self.right.increasedepth()

    def rightchild(self):
        return self.parent is not None and self.parent.right == self

    def leftchild(self):
        return self.parent is not None and self.parent.left == self

    def top(self):
        return self.parent is None

    def addright(self, val):
        pair = self
        # while we're a right chlid, chase parent
        # pointers until we're a left child or
        # we reach the top
        while pair.rightchild():
            pair = pair.parent

        # we've reached the root so we were the
        # leftmost node -- nothing to do
        if pair.parent is None:
            pass
        elif isinstance(pair.parent.right, int):
            pair.parent.right += val
        else:
            pair = pair.parent.right
            while not isinstance(pair.left, int):
                pair = pair.left
            pair.left += val
        
    def addleft(self, val):
        pair = self
        # while we're a left chlid, chase parent
        # pointers until we're a right child or
        # we reach the top
        while pair.leftchild():
            pair = pair.parent

        # we've reached the root so we were the
        # leftmost node -- nothing to do
        if pair.parent is None:
            pass
        elif isinstance(pair.parent.left, int):
            pair.parent.left += val
        else:
            pair = pair.parent.left
            while not isinstance(pair.right, int):
                pair = pair.right
            pair.right += val
            
    def __str__(self):
        return "[{},{}]".format(self.left, self.right)
    
    def explode(self):
        self.addleft(self.left)
        self.addright(self.right)
        if self.leftchild():
            self.parent.left = 0
        else:
            self.parent.right = 0

    def splitleftp(self):
        return isinstance(self.left, int) and self.left >= 10

    def splitrightp(self):
        return isinstance(self.right, int) and self.right >= 10    
    
    def splitleft(self):
        self.left = Pair(self.left//2, math.ceil(self.left/2),
                         depth=self.depth+1, parent=self)

    def splitright(self):
        self.right = Pair(self.right//2, math.ceil(self.right/2),
                         depth=self.depth+1, parent=self)


    def reduce(self):
        split = True
        while split:
            exploded = True
            while exploded:
                if not self.reduce_explode():
                    exploded = False

            if not self.reduce_split():
                split = False
            
        
    def reduce_split(self):

        if self.splitleftp():
            self.splitleft()
            return True
        if not isinstance(self.left, int):
            if self.left.reduce_split():
                return True

        if self.splitrightp():
            self.splitright()
            return True
        if not isinstance(self.right, int):
            if self.right.reduce_split():
                return True

        return False
        
    def reduce_explode(self):

        if self.depth == 4:
            self.explode()
            return True

        if not isinstance(self.left, int):
            if self.left.reduce_explode():
                return True
    
        if not isinstance(self.right, int):
            if self.right.reduce_explode():
                return True

        return False

    def mag(self):

        left = None
        right = None
        
        if isinstance(self.left, int):
            left = 3*self.left
        else:
            left = 3*self.left.mag()

        if isinstance(self.right, int):
            right = 2*self.right
        else:
            right = 2*self.right.mag()

        return left + right
            
def linetopair(line):
    if len(line) == 1:
        return int(line[0])

    line = line[1:len(line)-1]
    stack = 0
    i = 0
    for c in line:
        if c == '[':
            stack += 1
        elif c == ']':
            stack -= 1
        # we've found the center "," 
        elif c == "," and stack == 0:
            return Pair(linetopair(line[:i]),
                        linetopair(line[i+1:]))
        i += 1
        
if __name__ == '__main__':
    total = None
    for line in sys.stdin:
        if total is None:
            total = linetopair(line.strip())
        else:
            total = Pair(total, linetopair(line.strip()))

        total.reduce()

    print()
    print(total)
    print(total.mag())
        
