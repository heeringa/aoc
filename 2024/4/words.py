import sys


def collectstr(x,y,grid,dir):
    w = len(grid[0])
    h = len(grid)
    s = grid[y][x]
    for i in range(3):
        x,y = nextcoord(x,y,dir)
        if x < w and x >= 0 and y < h and y >= 0:
            s += grid[y][x]
    return s


def nextcoord(x,y,dir):
    if dir == "U":
        return x,y-1
    if dir == "UR":
        return x+1,y-1
    if dir == "R":
        return x+1,y
    if dir == "DR":
        return x+1,y+1
    if dir == "D":
        return x,y+1
    if dir == "DL":
        return x-1,y+1
    if dir == "L":
        return x-1,y
    if dir == "UL":
        return x-1,y-1


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        grid = [list(line.strip()) for line in fin]
        print(grid)
        print(collectstr(0,0,grid,"U"))
        w = len(grid[0])
        h = len(grid)

        evals = []
        for i in range(w):
            for j in range(h):
                for dir in ["U", "UR", "R", "DR", "D", "DL", "L", "UL"]:
                    evals.append(collectstr(i,j,grid,dir))
        
        count = 0
        for s in evals:
            if s == 'XMAS':
                count += 1
        print(count)

