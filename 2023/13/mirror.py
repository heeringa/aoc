import sys

def same(A, B):
    return all(a == b for a, b in zip(A, B))

def transpose(X):
    return [row for row in zip(*X)]

def reflect(rows):
    for i in range(len(rows)-1):
        reflect = True
        for j in range(min(i+1, len(rows)-i-1)):
            if not same(rows[i+1+j], rows[i-j]):
                reflect = False
                break
        if reflect:
            return i
    return None

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read()
        grids = lines.split("\n\n")

        total = 0
        for grid in grids:
            rows = [list(line.strip()) for line in grid.strip().split("\n")]

            i = reflect(rows)
            if i is not None:
                total += (i+1)*100

            cols = transpose(rows)

            i = reflect(cols)
            if i is not None:
                total += (i+1)

        print(total)



