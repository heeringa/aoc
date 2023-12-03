import sys

def symb(x):
    return (not x.isdigit()) and (x != '.')

def adj(grid, xa, xb, y):
    W = len(grid[0])
    H = len(grid)
    for x in range(xa-1, xb+2):
        if x >= 0 and x < W:
            if y-1 >= 0 and symb(grid[y-1][x]):
                return True
            if y+1 < H and symb(grid[y+1][x]):
                return True
    if xa-1 >= 0 and symb(grid[y][xa-1]):
        return True
    if xb+1 < W and symb(grid[y][xb+1]):
        return True
    return False
                    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = [line.strip() for line in f]
        nums = []
        for j,line in enumerate(grid):
            left = None
            right = None
            for i,c in enumerate(line):
                if c.isdigit():
                    if left is None:
                        left = i
                        right = i
                    if left is not None:
                        right = i
                else:
                    if left is not None:
                        print("Found Digit: {} at {}:{},{}".format("".join(line[left:right+1]), left, right, j))
                        if adj(grid, left, right, j):
                            nums.append(int("".join(line[left:right+1])))
                        left = None
                        right = None
            if left is not None:
                print("Found Digit: {} at {}:{},{}".format("".join(line[left:right+1]), left, right, j))
                if adj(grid, left, right, j):
                    nums.append(int("".join(line[left:right+1])))
                left = None
                right = None
        print(nums)
        print(sum(nums))
        

                    