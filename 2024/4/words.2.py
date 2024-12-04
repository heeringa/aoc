import sys


def collectstr(x,y,grid,dir):
    w = len(grid[0])
    h = len(grid)
    s = grid[y][x]
    for i in range(2):
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
        w = len(grid[0])
        h = len(grid)

        count = 0
        for i in range(w-2):
            for j in range(h-2):
                d1 = collectstr(i,j,grid,"DR")
                d2 = collectstr(i,j+2,grid,"UR")
                if (d1 == "MAS" or d1[::-1] == "MAS") and (d2 == "MAS" or d2[::-1] == "MAS"):
                    count += 1

        print(count)

