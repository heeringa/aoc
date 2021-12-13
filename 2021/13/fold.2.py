import sys

def foldup(pts, dim):
    newpts = set()
    for x,y in pts:
        if y <= dim:
            newpts.add((x,y))
        else:
            diff = y-dim
            newpts.add((x,dim-diff))
    return newpts

def foldleft(pts, dim):
    newpts = set()
    for x,y in pts:
        if x <= dim:
            newpts.add((x,y))
        else:
            diff = x-dim
            newpts.add((dim-diff,y))
    return newpts    
    
if __name__ == '__main__':
    pts = set()
    folds = []
    for line in sys.stdin:
        if line.startswith('f'):
            fold = line.strip()[len('fold along '):]
            folds.append((fold[0],int(fold[2:])))
            
        elif line != '\n':
            pair = line.strip().split(',')
            pts.add((int(pair[0]),int(pair[1])))

    for (dim,mag) in folds:
        if dim == 'y':
            pts = foldup(pts, mag)
        else:
            pts = foldleft(pts, mag)
            
    w = max(x for x,y in pts)+1
    h = max(y for x,y in pts)+1

    matrix = [['.']*w for _ in range(h)]

    for x,y in pts:
        matrix[y][x] = '*'

    for line in matrix:
        print("".join(line))

