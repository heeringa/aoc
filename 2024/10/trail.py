import sys
import queue

def adj(x,y,gid,w,h):
    if x > 0:
        if grid[y][x-1] == grid[y][x] - 1:
            yield x-1,y
    if x < w-1:
        if grid[y][x+1] == grid[y][x] - 1:
            yield x+1,y
    if y>0:
        if grid[y-1][x] == grid[y][x] - 1:        
            yield x,y-1
    if y < h-1:
        if grid[y+1][x] == grid[y][x] - 1:        
            yield x,y+1

def bfs(start, grid, w, h):
    closed = set()
    zeroes = set()
    Q = queue.Queue()
    Q.put(start)
    while not Q.empty():
        x,y = Q.get()
        for x2,y2 in adj(x,y,grid,w,h):
            #print("Evaluating ({}.{}) adj to ({},{})".format(x2,y2,x,y))
            if (x2,y2) not in closed:
                Q.put((x2,y2))
                if grid[y2][x2] == 0:
                    zeroes.add((x2,y2))
    return zeroes

if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        sizes = {}

        grid = [[int(i) for i in line.strip()] for line in fin]
        w = len(grid[0])
        h = len(grid)
        nines = set()
        for i in range(w):
            for j in range(h):
                if grid[j][i] == 9:
                    nines.add((i,j))
        print(nines)
        zeroes = set()
        for x,y in nines:
            zs = bfs((x,y),grid,w,h)
            for i,j in zs:
                sizes[(i,j)] = sizes.get((i,j),0) + 1
            print("{},{}: {}".format(x,y,zs))
            zeroes = zeroes.union(zs)
        print(zeroes)
        print(sizes)
        print(sum(sizes.values()))
