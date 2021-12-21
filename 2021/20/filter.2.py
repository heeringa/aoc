import sys


def addborder(matrix, size=3):
    h = len(matrix)
    w = len(matrix[0])
    new = [[0]*(w+2*size) for _ in range(h+(2*size))]
    for i in range(h):
        for j in range(w):
            new[i+size][j+size] = matrix[i][j]
    return new

def shrinkboarder(matrix, size=10):
    h = len(matrix)
    w = len(matrix[0])
    new = [[0]*(w-2*size) for _ in range(h-(2*size))]
    for i in range(len(new)):
        for j in range(len(new[0])):
            new[i][j] = matrix[i+size][j+size]
    return new
    
def itergrid(x, y):

    yield x-1,y-1
    yield x-1,y
    yield x-1,y+1
    yield x,y-1
    yield x,y
    yield x,y+1
    yield x+1,y-1
    yield x+1,y
    yield x+1,y+1
        

def grid2int(matrix, x, y, enhance):
    index = int("".join(str(z) for z in [matrix[i][j] for i,j in itergrid(x,y)]),2)
    return 1 if enhance[index] == 1 else 0
        
def old2new(matrix, enhance):
    m2 = [line[:] for line in matrix]
    for i in range(1,len(matrix)-1):
        for j in range(1,len(matrix[0])-1):
            m2[i][j] = grid2int(matrix, i, j, enhance)
    return m2

def printmatrix(m):

    def bin2chr(c):
        return '.' if c == 0 else '#'
    
    for line in m:
        print("".join(bin2chr(i) for i in line))
    print()
    

if __name__ == '__main__':
    def chr2bin(c):
        return 0 if c == '.' else 1

    enhance = [chr2bin(c) for c in sys.stdin.readline().strip()]

    sys.stdin.readline()
    matrix = []
    for line in sys.stdin:
        matrix.append([chr2bin(c) for c in line.strip()])


    print(enhance)
    printmatrix(matrix)
    print()
    print("--")

    for i in range(25):
        matrix = addborder(matrix,10)
#        printmatrix(matrix)
#        print()    
        matrix = old2new(matrix, enhance)
        matrix = addborder(matrix,10)
#        printmatrix(matrix)
#        print()    
        matrix = old2new(matrix, enhance)               
        matrix = shrinkboarder(matrix,15)        
        print(i)
        print()
    print("--")
    
    total = sum(sum(line) for line in matrix)
    print(total)
    
    
    
