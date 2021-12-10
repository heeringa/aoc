import sys

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
    print(val)
    return True
    
    
if __name__ == '__main__':
    matrix = []
    for line in sys.stdin:
        matrix.append([int(d) for d in line.strip()])
    width = len(matrix[0])
    height = len(matrix)

    total = 0
    for line in matrix:
        print(line)
    for x in range(height):
        for y in range(width):
            neighbors = list(iterneighbors(matrix,x,y,width,height))
            #print("{},{} has neigbors {}".format(x,y,neighbors))
            neighbor_vals = [matrix[i][j] for i,j in neighbors]
            if (lowpoint(matrix[x][y], neighbor_vals)):
                total = total + matrix[x][y] + 1
    print(total)
    
