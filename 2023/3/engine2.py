import sys

def symb(x):
    return x == '*'

def adj(grid, xa, xb, y):
    stars = []
    W = len(grid[0])
    H = len(grid)
    for x in range(xa-1, xb+2):
        if x >= 0 and x < W:
            if y-1 >= 0 and symb(grid[y-1][x]):
                stars.append((x,y-1))
            if y+1 < H and symb(grid[y+1][x]):
                stars.append((x,y+1))
    if xa-1 >= 0 and symb(grid[y][xa-1]):
        stars.append((xa-1,y))
    if xb+1 < W and symb(grid[y][xb+1]):
        stars.append((xb+1,y))
    return stars
                    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        grid = [line.strip() for line in f]
        stars = {}
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
                        digit = int("".join(line[left:right+1]))
                        print("Found Digit: {} at {}:{},{}".format(digit, left, right, j))
                        for star in adj(grid, left, right, j):
                            stars.setdefault(star, []).append(digit)
                        left = None
                        right = None
            if left is not None:
                digit = int("".join(line[left:right+1]))
                print("Found Digit: {} at {}:{},{}".format(digit, left, right, j))
                for star in adj(grid, left, right, j):
                    stars.setdefault(star, []).append(digit)                

        print(stars)
        total = 0
        for star,nums in stars.items():
            if len(nums) == 2:
                total += nums[0] * nums[1]
        print(total)

                    