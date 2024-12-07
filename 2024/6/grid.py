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
        visited = set()
        while not escaped(x,y,w,h):
            visited.add((x,y))
            while blockedahead(x,y,grid,dir):
                dir = turnright(x,y,dir)
            x,y = move(x,y,dir)
        
        for x,y in visited:
            grid[y][x] = "X"
        
        print("\n".join(["".join(row) for row in grid]))
        print(len(visited))