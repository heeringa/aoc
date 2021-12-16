import sys

def iterneighbors(x, y, w, h):
    # up
    if x != 0:
        yield x-1,y

        # TL Diag
#        if y != 0:
 #           yield x-1,y-1
        # TR Diag
#        if y != w-1:
#            yield x-1,y+1
    # down
    if x != h-1:
        yield x+1,y

        # BL Diag
#        if y != 0:
#            yield x+1,y-1
        # BR Diag
#        if y != w-1:
#            yield x+1,y+1
        
    # left
    if y != 0:
        yield x,y-1
    # right
    if y != w-1:
        yield x,y+1

    

        
def shortestpath(risks):
    spds = [[None]*len(risks[0]) for _ in range(len(risks))]
    parents = [[None]*len(risks[0]) for _ in range(len(risks))]
    frontier = []
    w = len(risks[0])
    h = len(risks)
    size = w*h

    frontier.append((0,0))
    spds[0][0] = 0
    while frontier:
        # greedily choose the node that crosses
        # the cut according to shortest path dist est
        node = frontier.pop()
        nx,ny = node
        for mx,my in iterneighbors(nx,ny,w,h):
            # add all neighbors of node to the frontier
            # if they aren't there already
            if spds[mx][my] == None:
                spds[mx][my] = spds[nx][ny] + risks[mx][my]
                parents[mx][my] = (nx,ny)
                frontier.append((mx,my))

            # if a neighbor is already in the frontier, it's
            # SPDS might improve
            elif (mx,my) in frontier:
                dist = spds[nx][ny] + risks[mx][my]
                if dist < spds[mx][my]:
                    spds[mx][my] = diist
                    parents[mx][my] = (nx,ny)

        def dist(node):
            x,y = node
            return spds[x][y]

        frontier.sort(key=dist, reverse=True)

    return spds,parents
    
        

if __name__ == '__main__':
    risks = [[int(i) for i in line.strip()] for line in sys.stdin]
    spds, parents = shortestpath(risks)
    w = len(risks[0])
    h = len(risks)
    print(spds[h-1][w-1])

        

    
