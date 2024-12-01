import sys
import timeit



def adj(node, grid, factory):
    #print("Attempting to find ADJ nodes of {}".format(node))
    x, y, dir = node.x, node.y, node.d
    if dir == 'right' and x < len(grid[0]) - 1 and node.step < 3:
        #print("R")
        yield factory.node(x+1, y, dir, node.step + 1)
    if dir == 'left' and x > 0 and node.step < 3:
        #print("L")                
        yield factory.node(x-1, y, dir, node.step + 1)
    if dir == 'up' and y > 0 and node.step < 3:
        #print("U")        
        yield factory.node(x, y-1, dir, node.step + 1)
    if dir == 'down' and y < len(grid) - 1 and node.step < 3:
        #print("D")        
        yield factory.node(x, y+1, dir, node.step + 1)
    if x > 0 and (dir == 'down' or dir == 'up'):
        #print("L")
        yield factory.node(x-1, y, 'left', 1)
    if x < len(grid[0]) - 1 and (dir == 'down' or dir == 'up'):
        #print("R")
        yield factory.node(x+1, y, 'right', 1)
    if y > 0 and (dir == 'right' or dir == 'left'):
        #print("U")
        yield factory.node(x, y-1, 'up', 1)
    if y < len(grid) - 1 and (dir == 'right' or dir == 'left'):
        #print("D")
        yield factory.node(x, y+1, 'down', 1)


class NodeFactory:

    def __init__(self, grid):
        self.grid = grid
        self.nodes = {}
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                for z in range(3):
                    for d in ['up', 'down', 'left', 'right']:
                        self.nodes[(x, y, d, z+1)] = Node(x, y, d, grid[y][x], z+1)

        # add a special source node
        self.nodes[(0, 0, 'right', 0)] = Node(0, 0, 'right', 0, 0, 0)
        self.nodes[(0, 0, 'down', 0)] = Node(0, 0, 'down', 0, 0, 0)

    def node(self, x, y, d, step):
        return self.nodes[(x, y, d, step)]
    

class Node:

    def __init__(self, x, y, direction, val, step, dist=None):
        self.x = x
        self.y = y
        self.d = direction
        self.val = val
        self.step = step
        self.dist = dist

    def __hash__(self):
        return hash((self.x, self.y, self.d, self.step))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.step == other.step and self.d == other.d

    def __str__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.d, self.step)

    def __repr__(self):
        return self.__str__()

def shortest(grid):
    
    factory = NodeFactory(grid)
    sr = factory.node(0, 0, 'right', 0)
    sd = factory.node(0, 0, 'down', 0)
    closed = set()
    closed.add(sr)
    closed.add(sd)
    open = set()
    
    for n in adj(sr, grid, factory):
        n.dist = sr.dist + n.val
        open.add(n)
    for n in adj(sd, grid, factory):
        n.dist = sd.dist + n.val
        open.add(n)

    print(open)

    goal = None
    while goal is None:
        #print(timeit.timeit(lambda: sorted(open, key=lambda x: x.dist).pop(0)))
        node = sorted(open, key=lambda x: x.dist).pop(0)
        open.remove(node)
        print("Found closed node {} with minimal distance {}".format(node, node.dist))
        for adj_node in adj(node, grid, factory):
            #print("Adj node: {}".format(adj_node))
            if adj_node not in closed:
                # adjust the dist estimate if necessary
                est = node.dist + adj_node.val
                if adj_node.dist is None or est < adj_node.dist:
                    adj_node.dist = est
                # add the node to open -- might be there already
                open.add(adj_node)
            closed.add(node)
            if node.x == len(grid[0]) - 1 and node.y == len(grid) - 1:
                goal = node
                break
        #print("Closed: {}".format(closed))
    
    return goal.dist

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        grid = [[int(i) for i in line.strip()] for line in f]
        d = shortest(grid)
        print(d)