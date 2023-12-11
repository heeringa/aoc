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
        
        for (x,y),v in dist.items():
            print("({},{}) = {}".format(x,y,v))

        print(max(dist.values()))
