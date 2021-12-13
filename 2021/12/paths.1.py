import sys

def DFS(node, adj, visited, small):

    if node == 'end':
        return 1    
    total = 0
    for neighbor in adj[node]:
        if not (neighbor in visited):
            if neighbor in small:
                visited.add(neighbor)            
            total += DFS(neighbor, adj, visited, small)
            if neighbor in small:
                visited.remove(neighbor)
            
    return total
    
if __name__ == '__main__':
    adj = {}
    small = set()
    for line in sys.stdin:
        pair = line.strip().split('-')
        start = pair[0]
        end = pair[1]

        # add the small nodes to the set
        if start.lower() == start:
            small.add(start)
        if end.lower() == end:
            small.add(end)

        # create the adjacecy list
        adjlist = adj.setdefault(start,[])
        adjlist.append(end)

        adjlist = adj.setdefault(end,[])
        adjlist.append(start)

    visited = set()
    visited.add('start')

    total = DFS('start', adj, visited, small)
    print(total)
