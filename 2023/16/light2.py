import sys

sys.setrecursionlimit(1000*1000)

def splitx(x, y, dir, rows):
    return rows[y][x] == '-' and (dir == 'down' or dir == 'up')

def splity(x, y, dir, rows):
    return rows[y][x] == '|' and (dir == 'left' or dir == 'right')

def moveup(x,y,dir,rows):
    return ((rows[y][x] == '.' or rows[y][x] == '|')and dir == 'up') or \
           (rows[y][x] == '\\' and dir == 'left') or \
           (rows[y][x] == '/' and dir == 'right')

def movedown(x,y,dir,rows):
    return ((rows[y][x] == '.' or rows[y][x] == '|') and dir == 'down') or \
           (rows[y][x] == '\\' and dir == 'right') or \
           (rows[y][x] == '/' and dir == 'left')

def moveleft(x,y,dir,rows):
    return (rows[y][x] == '.' and dir == 'left') or \
           (rows[y][x] == '\\' and dir == 'up') or \
           (rows[y][x] == '/' and dir == 'down') or \
           (rows[y][x] == '-' and dir == 'left')

def moveright(x,y,dir,rows):
    return ((rows[y][x] == '.' or rows[y][x] == '-') and dir == 'right') or \
           (rows[y][x] == '\\' and dir == 'down') or \
           (rows[y][x] == '/' and dir == 'up')
            
                                                                                                      
def next(x, y, dir, rows):
    if splitx(x,y,dir,rows):
        ret = []
        if x > 0:
            ret.append((x-1, y, 'left'))
        if x < len(rows[y])-1:
            ret.append((x+1, y, 'right'))
        return ret
    if splity(x,y,dir,rows):
        ret = []
        if y > 0:
            ret.append((x, y-1, 'up'))
        if y < len(rows)-1:
            ret.append((x, y+1, 'down'))
        return ret
    if moveup(x,y,dir,rows):
        if y == 0:
            return []
        else:
            return [(x, y-1, 'up')]
    if movedown(x,y,dir,rows):
        if y == len(rows)-1:
            return []
        else:
            return [(x, y+1, 'down')]
    if moveleft(x,y,dir,rows):
        if x == 0:
            return []
        else:
            return [(x-1, y, 'left')]
    if moveright(x,y,dir,rows):
        if x == len(rows[y])-1:
            return []
        else:
            return [(x+1, y, 'right')]
        
def viz(prez, x, y, dir):
    if prez[y][x] == '.':
        if dir == 'right':
            prez[y][x] = '>'
        if dir == 'left':
            prez[y][x] = '<'
        if dir == 'up':
            prez[y][x] = '^'
        if dir == 'down':
            prez[y][x] = 'v'


def getactivated(x,y,dir,rows,seen,cache):
    seen.add((x,y,dir))    
    if (x,y,dir) in cache:
        return cache[(x,y,dir)]
    else:
        ret = set()
        ret.add((x,y))
    
        for nx,ny,nd in next(x,y,dir,rows):
            if (nx,ny,nd) not in seen:
                ret = ret.union(getactivated(nx,ny,nd,rows,seen,cache))
        cache[(x,y,dir)] = ret
        return ret



if __name__ == '__main__':

    
    cache = {}

    with open(sys.argv[1]) as f:
        rows = [list(line.strip()) for line in f]
        prez = [row[:] for row in rows]

        best = 0
        for y in range(len(rows)):
            activated = getactivated(0,y,'right',rows, set(), {})
            print("{} Activated starting at {},{} moving {}".format(len(activated),0,y,'right'))
            best = max(best, len(activated))

            activated = getactivated(0,y,'right',rows, set(), {})
            print("{} Activated starting at {},{} moving {}".format(len(activated),0,y,'right'))
            best = max(best, len(activated))

            activated = getactivated(len(rows[0])-1,y,'left',rows, set(), cache)
            print("{} Activated starting at {},{} moving {}".format(len(activated),len(rows[0])-1,y,'left'))            
            best = max(best, len(activated))

        for x in range(len(rows[0])):
            activated = getactivated(x,0,'down',rows, set(), cache)
            print("{} Activated starting at {},{} moving {}".format(len(activated),x,0,'down'))            
            best = max(best, len(activated))
            activated = getactivated(x,len(rows)-1,'up',rows, set(), cache)
            print("{} Activated starting at {},{} moving {}".format(len(activated),x,len(rows)-1,'up'))            
            best = max(best, len(activated))
        
        print(best)
        #print(cache[(3,0,'down')])
