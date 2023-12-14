import sys

def same(A, B):
    misses = 0
    for a,b in zip(A,B):
        if a != b:
            misses += 1
    return misses

def transpose(X):
    return [row for row in zip(*X)]

def reflect(rows):
    for i in range(len(rows)-1):
        print("Consider reflection between {} and {}".format(i,i+1))        
        misses = 0
        for j in range(min(i+1, len(rows)-i-1)):
            misses += same(rows[i+1+j], rows[i-j])
        if misses == 1:
            print("Found reflection between {} and {} has 1 miss".format(i,i+1))
            return i
    return None
            

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read()
        grids = lines.split("\n\n")

        total = 0
        for grid in grids:
            print(grid)
            rows = [list(line.strip()) for line in grid.strip().split("\n")]
        
            for i,row in enumerate(rows):
                print("{} {}".format(i,row))


            i = reflect(rows)
            if i is not None:
                total += (i+1)*100

            cols = transpose(rows)

            i = reflect(cols)
            if i is not None:
                total += (i+1)

        print(total)



