import sys

def det_start(x, y, graph):
    W = len(graph[0]) 
    H = len(graph) 
    UP = False
    DOWN = False 
    RIGHT = False
    LEFT = False
    if y > 0 and graph[y-1][x] in ['|', 'F', '7']:
        UP = True
    if y < H-1 and graph[y+1][x] in ['|', 'J', 'L']:
        DOWN = True
    if x > 0 and graph[y][x-1] in ['-', 'F', 'L']:
        LEFT = True
    if x < W-1 and graph[y][x+1] in ['-', '7', 'J']:
        RIGHT = True

    if UP:
        if LEFT:
            return 'J'
        if RIGHT:
            return 'L'
        if DOWN:
            return '|'
    if DOWN:
        if LEFT:
            return '7'
        if RIGHT:
            return 'F'
    if LEFT and RIGHT:
        return '-' 


def flood(x, y, graph):
    W = len(graph[0]) 
    H = len(graph) 
    if y > 0 and graph[y-1][x] == 0:
        # up
        yield (x,y-1)
    if y < H-1 and graph[y+1][x] == 0:
        # down
        yield (x,y+1)
    if x > 0 and graph[y][x-1] == 0:
        # left
        yield (x-1,y)
    if x < W-1 and graph[y][x+1] == 0:
        # RIGHT = True
        yield (x+1,y)


def neighbors(x, y, graph):
    if graph[y][x] in ['|', 'J', 'L']:
        # up
        yield (x,y-1)
    if graph[y][x] in ['-', 'L', 'F']:
        # right
        yield (x+1,y)
    if graph[y][x] in ['|', 'F', '7']:
        # down
        yield (x,y+1)
    if graph[y][x] in ['-', 'J', '7']:
        # left
        yield (x-1,y)
    


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        graph = [list(row.strip()) for row in f.readlines()]
        print(graph)
        start = None
        for y in range(len(graph)):
            for x in range(len(graph[y])):
                if graph[y][x] == 'S':
                    start = (x, y)
                    graph[y][x] = det_start(x, y, graph)
                    break   
        
        print(graph)

        Q = [start]
        dist = {start: 0}
        while len(Q) > 0:
            x,y = Q.pop(0)
            for x2, y2 in neighbors(x, y, graph):
                if (x2, y2) not in dist:
                    Q.append((x2,y2))
                    dist[(x2,y2)] = dist[(x,y)] + 1
        
        superg = [(2*len(graph[0])+1)*[0] for _ in range(2*len(graph)+1)]
        
        for x,y in dist.keys():
            superg[2*y+1][2*x+1] = 1
            for x2,y2 in neighbors(x,y,graph):
                superg[y2+y+1][x2+x+1] = 1

        for row in superg:
            print(row)

        Q = [(0,0)]
        while len(Q) > 0:
            x,y = Q.pop(0)
            for x2, y2 in flood(x, y, superg):
                superg[y2][x2] = 1
                Q.append((x2,y2))

        for row in superg:
            print(row)

        total = 0
        for y in range(len(superg)):
            for x in range(len(superg[y])):
                if superg[y][x] == 0 and (x % 2 == 1) and (y % 2) == 1:
                    total += 1
        
        print(total)








