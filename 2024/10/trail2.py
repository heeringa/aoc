import sys
import queue

def adj(x,y,gid,w,h):
    if x > 0:
        if grid[y][x-1] == grid[y][x] + 1:
            yield x-1,y
    if x < w-1:
        if grid[y][x+1] == grid[y][x] + 1:
            yield x+1,y
    if y>0:
        if grid[y-1][x] == grid[y][x] + 1:        
            yield x,y-1
    if y < h-1:
        if grid[y+1][x] == grid[y][x] + 1:        
            yield x,y+1

if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        grid = [[int(i) for i in line.strip()] for line in fin]
        w = len(grid[0])
        h = len(grid)

        heights = {i:[] for i in range(10)}
        trails = [[0]*w for _ in range(h)]
        nines = set()
        for i in range(w):
            for j in range(h):
                heights[grid[j][i]].append((i,j))

        for x,y in heights[0]:
            trails[y][x] = 1

        print(heights)
        print(trails)

        for height in range(10):
            for x,y in heights[height]:
                for x2,y2 in adj(x,y,grid,w,h):
                    trails[y2][x2] += trails[y][x]
        
        print(trails)
        print(sum(trails[y][x] for x,y in heights[9]))

