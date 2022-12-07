import sys


class Node:

    def __init__(self, name, size, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {}
        self.direcs = {}

    def updateSize(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.updateSize(size)
            
    def addChild(self, name, size):
        self.children[name] = Node(name, size, self)
        self.updateSize(size)

    def addDirectory(self, name):
        self.direcs[name] = Node(name, 0, self)

    def cd(self, name):
        return self.direcs[name]

    def nodesWith(self, diff):
        if self.size >= diff:
            rec = [(self.name, self.size)]
        else:
            rec = []
        for k,v in self.direcs.items():
            rec.extend(v.nodesWith(diff))
        return rec
            
def parse(lines):
    root = Node('/', 0)
    cur = root
    for line in f:
        if line.startswith('$'):
            line = line[2:]
            if line.startswith("cd"):
                l,r = line.split()
                if r == '/':
                    cur = root
                elif r == '..':
                    cur = cur.parent
                else:
                    cur = cur.cd(r)
        else:
            l,r = line.strip().split()
            if l == 'dir':
                cur.addDirectory(r)
            else:
                cur.addChild(r, int(l))

    return root
                
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        root = parse(f)
        free = 70000000 - root.size
        diff = 30000000 - free
        nodes = root.nodesWith(diff)
        print(min(nodes, key=lambda x: x[1]))
                    
