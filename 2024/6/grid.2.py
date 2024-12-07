import sys

def move(x,y,dir):
    if dir == "^":
        return x,y-1
    if dir == "v":
        return x,y+1
    if dir == ">":
        return x+1,y
    if dir == "<":
        return x-1,y
    
def blockedahead(x,y,grid,dir):
    x,y = move(x,y,dir)
    if not escaped(x,y,len(grid[0]),len(grid)):
        return grid[y][x] == '#'
    else:
        return False

def turnright(x,y,dir):
    dirs = ["^",">","v","<"]
    return dirs[(dirs.index(dir)+1) % 4]
    
def findstart(grid,w,h):
    for j in range(h):
        for i in range(w):
            if grid[j][i] in ["<", ">", "v", "^"]:
                return i,j,grid[j][i]

def escaped(x,y,w,h):
    return x >= w or x < 0 or y >= h or y < 0
            
if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        grid = [list(line.strip()) for line in fin]
        w = len(grid[0])
        h = len(grid)
        x,y,dir = findstart(grid,w,h)
        
        startx = x
        starty = y
        startdir = dir

        visited = set()
        while not escaped(x,y,w,h):
            visited.add((x,y))
            while blockedahead(x,y,grid,dir):
                dir = turnright(x,y,dir)
            x,y = move(x,y,dir)
        

        
        locs = set()
        for (i,j) in visited:
            grid[j][i] = "#"
            cycle = set()
            x = startx
            y = starty
            dir = startdir
            while not escaped(x,y,w,h):
                if (x,y,dir) in cycle:
                    locs.add((i,j))
                    break
                cycle.add((x,y,dir))
                while blockedahead(x,y,grid,dir):
                    dir = turnright(x,y,dir)
                x,y = move(x,y,dir)
            
            grid[j][i] = '.'


        print(locs)
        print(len(locs))