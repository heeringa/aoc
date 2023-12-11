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
    newrows = []
    for row in grid:
        if all(c == '.' for c in row):
            newrows.append(['.'] * len(row))
        newrows.append(row)
    return newrows

def points(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                yield (x, y)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = [list(line.strip()) for line in f.readlines()]
        g2 = transpose(expandrows(transpose(expandrows(grid))))
        pts = [p for p in points(g2)]
        for pt in pts:
            print(pt)

        total = 0
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                x1, y1 = pts[i]
                x2, y2 = pts[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                total += dist
                print("Dist ({},{}) to ({},{}) = {}".format(x1, y1, x2, y2, dist))
        print(total)
