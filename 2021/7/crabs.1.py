import sys


if __name__ == '__main__':
    crabs = [int(p) for p in sys.stdin.readline().split(',')]
    minp = min(crabs)
    maxp = max(crabs)
    minfuel = None
    for pos in range(minp, maxp+1):
        dist = 0
        for crab in crabs:
            dist = dist + abs(crab-pos)
        if minfuel is None or dist < minfuel:
            minfuel = dist
    print(minfuel)
