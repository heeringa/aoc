import sys

def assign(matrix, x, y, w, h, basins, basinid):
    if matrix[x][y] != 9 and basins[x][y] == 0:
        basins[x][y] = basinid
        size = 0
        for i,j in iterneighbors(matrix, x, y, w, h):
            size = assign(matrix, i, j, w, h, basins, basinid)
        return size+1
    else:
        return 0
    
def iterneighbors(matrix, x, y, w, h):
    print("Pt = {},{} with w={} h={}".format(x,y,w,h))
    # up
    if x != 0:
        yield x-1,y
    # down
    if x != h-1:
        yield x+1,y
    # left
    if y != 0:
        yield x,y-1
    # right
    if y != w-1:
        yield x,y+1

def lowpoint(val, vals):
    for v in vals:
        if val >= v:
            return False
    return True
    
    
if __name__ == '__main__':
    matrix = []
    for line in sys.stdin:
        matrix.append([int(d) for d in line.strip()])
    width = len(matrix[0])
    height = len(matrix)

    minima = []
    for x in range(height):
        for y in range(width):
            neighbors = list(iterneighbors(matrix,x,y,width,height))
            neighbor_vals = [matrix[i][j] for i,j in neighbors]
            if (lowpoint(matrix[x][y], neighbor_vals)):
                minima.append((x,y))

    basins = [[0]*width for _ in range(height)]
    basinid = 1
    for x,y in minima:
        assign(matrix, x, y, width, height, basins, basinid)
        basinid += 1

    basincounts = {}
    for x in range(height):
        for y in range(width):
            cnt = basincounts.get(basins[x][y],0)
            basincounts[basins[x][y]] = cnt + 1

    sizes = sorted([v for k,v in basincounts.items() if k != 0], reverse=True)

    print(sizes[0] * sizes[1] * sizes[2])


    
