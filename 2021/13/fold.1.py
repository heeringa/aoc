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

    
    dim,mag = folds[0]
    if dim == 'y':
        pts = foldup(pts, mag)
    else:
        pts = foldleft(pts, mag)
            
    print(len(pts))
