import sys

def iterneighbors(x, y, w, h):
    # up
    if x != 0:
        yield x-1,y

        # TL Diag
        if y != 0:
            yield x-1,y-1
        # TR Diag
        if y != w-1:
            yield x-1,y+1
    # down
    if x != h-1:
        yield x+1,y

        # BL Diag
        if y != 0:
            yield x+1,y-1
        # BR Diag
        if y != w-1:
            yield x+1,y+1
        
    # left
    if y != 0:
        yield x,y-1
    # right
    if y != w-1:
        yield x,y+1

    
def day(levels):
    w = len(levels[0])
    h = len(levels)
    flashes = []
    nextlevels = []
    totalflashes = 0
    
    print(w,h)
    
    for x in range(h):
        newrow = []
        for y in range(w):
            newlevel = (levels[x][y]+1) % 10
            newrow.append(newlevel)
            if newlevel == 0:
                flashes.append((x,y))
                totalflashes += 1
        nextlevels.append(newrow)

    while flashes:
        x,y = flashes.pop()
        for i,j in iterneighbors(x,y,w,h):
            level = nextlevels[i][j]
            if level != 0:
                newlevel = (level + 1) % 10
                nextlevels[i][j] = newlevel
                if newlevel == 0:
                    totalflashes += 1
                    flashes.append((i,j))

    return nextlevels,totalflashes,totalflashes == w*h
            

if __name__ == '__main__':
    levels = [[int(i) for i in list(line.strip())] for line in sys.stdin]
    days = 200
    totalflashes = 0
    firstflash = None
    
    print("Before any steps:")
    for row in levels:
        print(row)
    print()
    
    for d in range(days):
        levels,flashes,allflashed = day(levels)
        totalflashes += flashes
        if allflashed and not firstflash:
            firstflash = d+1
        print("After step {} flashes = {}".format(d+1, flashes))
        for row in levels:
            print(row)
        print()

    print(totalflashes,firstflash)
    
