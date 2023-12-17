import sys

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


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        rows = [list(line.strip()) for line in f]
        prez = [row[:] for row in rows]

        pts = [(0,0,'right')]
        activated = set()
        activated.add((0,0))
        seen = set()
        seen.add((0,0,'right'))
        while len(pts) > 0:
            newpts = []
            for x,y,d in pts:
                activated.add((x,y))
                for nx,ny,nd in next(x,y,d,rows):
                    print("Moving from {} {} to {} {} on {}".format(x,y,nx,ny,rows[y][x]))                 
                    if (nx,ny,nd) in seen:                    
                        print("Collision at {} {}".format(nx, ny))
                    else:
                        seen.add((nx,ny,nd))
                        newpts.append((nx,ny,nd))
            pts = newpts
            for (x,y,dir) in seen:
                viz(prez, x, y, dir)


        for row in rows:
            print("".join(row))
        print()
        for row in prez:
            print("".join(row))
        print(len(activated))

