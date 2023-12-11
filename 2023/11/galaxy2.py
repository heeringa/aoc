import sys


def transpose(grid):
    W = len(grid[0])
    H = len(grid)
    g2 = [[0] * H for _ in range(W)]
    for j in range(W):
        for i in range(H):
            g2[j][i] = grid[i][j]
    return g2


def expandrows(grid):
    expanded = []
    for i, row in enumerate(grid):
        if all(c == '.' for c in row):
            expanded.append(i)
    return set(expanded)

def points(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                yield (x, y)


if __name__ == '__main__':
    N = 1000000
    with open(sys.argv[1]) as f:
        grid = [list(line.strip()) for line in f.readlines()]
        rows = expandrows(grid)
        cols = expandrows(transpose(grid))

        print(rows)
        print(cols)

        pts = [p for p in points(grid)]
        for pt in pts:
            print(pt)

        total = 0
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                x1, y1 = pts[i]
                x2, y2 = pts[j]

                cs = set(range(min(x1,x2),max(x1,x2)+1))
                rs = set(range(min(y1,y2),max(y1,y2)+1))

                print("Column Range = {}".format(cs))
                print("Row Range = {}".format(rs))

                xint = cs.intersection(cols)
                yint = rs.intersection(rows)

                print("X Intersection = {}".format(xint))
                print("Y Intersection = {}".format(yint))


                xdist = len(xint)*N + abs(x1-x2) - len(xint)
                ydist = len(yint)*N + abs(y1-y2) - len(yint)

                print("X Dist = {}".format(xdist))
                print("Y Dist = {}".format(ydist))  

                dist = xdist + ydist

                total += dist

                print("Dist ({},{}) to ({},{}) = {}".format(x1, y1, x2, y2, dist))
        print(total)
