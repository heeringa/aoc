import sys


class CPU:

    def __init__(self, step=40):
        self.step = step
        self.cycle = 0
        self.strengths = []
        self.row = -1
        self.val = 1
        self.record()

    def add(self, v):
        self.advance()
        self.record()
        self.advance()
        self.val += v
        self.record()
        
        
    def noop(self):
        self.advance()
        self.record()
        
    def advance(self):
        self.cycle += 1

    def overlap(self, cycle):
        cycle = cycle % self.step
        return self.val-1 == cycle  or self.val == cycle or self.val+1 == cycle
    
    def record(self):
        if self.cycle % self.step == 0:
            self.row += 1
            self.strengths.append([])
            
        if self.overlap(self.cycle):
            self.strengths[self.row].append('#')
        else:
            self.strengths[self.row].append('.')
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        c = CPU()
        for line in f:
            op = line.strip().split()
            if op[0] == 'addx':
                c.add(int(op[1]))
            else:
                c.noop()
        
        print("\n".join(["".join(row) for row in c.strengths]))

        
        
