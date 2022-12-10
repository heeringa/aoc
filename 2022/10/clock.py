import sys


class CPU:

    def __init__(self, strengthstart = 20, stop=220, step=40):
        self.nextCheck = strengthstart
        self.stop = stop
        self.step = step
        self.cycle = 1
        self.strengths = []
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

    def record(self):
        if self.cycle == self.nextCheck:
            self.strengths.append(self.val* self.cycle)
            self.nextCheck += self.step
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        c = CPU()
        for line in f:
            op = line.strip().split()
            if op[0] == 'addx':
                c.add(int(op[1]))
            else:
                c.noop()
                
        print(sum(c.strengths))
