import sys


def makeChildren(rows):
    children = {}
    n = len(rows)
    m = len(rows[0])
    for i in range(n):
        for j in range(m):
            val = rows[i][j]
            children[(i,j)] = []
            # UP
            if i > 0:
                if (rows[i-1][j] - val) <= 1:
                    children[(i,j)].append((i-1,j))
            # DOWN
            if i < n-1:
                if (rows[i+1][j] - val) <= 1:
                    children[(i,j)].append((i+1,j))
            # RIGHT
            if j < m-1:
                if (rows[i][j+1] - val) <= 1:
                    children[(i,j)].append((i,j+1))
            # LEFT
            if j > 0:
                if (rows[i][j-1] - val) <= 1:
                    children[(i,j)].append((i,j-1))
    return children
            
    
def bfs(rows, children, start, finish):
    Q = [(start,0)]
    visited = set()
    steps = 0
    while len(Q) != 0:
        node,dist = Q.pop(0)
        if node == finish:
            return (node,dist)
        for child in children[node]:
            if child not in visited:
                Q.append((child,dist+1))
                visited.add(child)
    
    
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        rows = []
        start = None
        finish = None
        n = 0
        for line in f:
            m = 0
            row = []
            for i in list(line.strip()):
                if i == 'S':
                    start = (n,m)
                    row.append(0)
                elif i == 'E':
                    finish = (n,m)
                    row.append(25)
                else:
                    row.append(ord(i)-ord('a'))
                m += 1
            rows.append(row)
            n += 1

        children = makeChildren(rows)
        
        node, dist = bfs(rows, children, start, finish)
        print(node)
        print(dist)
        
            
            
