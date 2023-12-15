import sys


def transpose(X):
    return [list(x) for x in zip(*X)]

def rev(X):
    return [x[::-1] for x in X]

def west(rocks):
    
    def rollrowwest(row):
        newrow = []
        count = 0
        total = 0
        for i in range(len(row)):
            if row[i] == '#':
                newrow.extend(['O']*count)
                newrow.extend(['.']*(total-count))
                newrow.append('#')
                total = 0
                count = 0
            elif row[i] == 'O':
                count += 1
                total += 1
            else:
                total += 1
        newrow.extend(['O']*count)
        newrow.extend(['.']*(total-count))
        return newrow

    return [rollrowwest(row) for row in rocks]

def north(rocks):
    return transpose(west(transpose(rocks)))

def east(rocks):
    return rev(west(rev(rocks)))

def south(rocks):
    return transpose(rev(west(rev(transpose(rocks)))))


def score(rocks):

    def score_row(row, val):
        return sum(val for r in row if r == 'O')

    return sum(score_row(row, val) for row, val in zip(rocks, range(len(rocks), 0, -1)))

def pr(rocks):
    for row in rocks:
        print(''.join(row))

def tup(rocks):
    return tuple(tuple(row) for row in rocks)

def cycle(rocks):
    return east(south(west(north(rocks))))


# determine the cycle length from rocks back to itself
def cycle_length(store, rocks):
    t = tup(rocks)
    next = tup(store[t])
    i = 1

    while next != t:        
        next = tup(store[next])
        i += 1
    
    return i

if __name__ == '__main__':
    N = 1000000000
    with open(sys.argv[1]) as f:
        rocks = [list(line.strip()) for line in f]

        store = {}
        t = tup(rocks)
        
        # (r1) -> (r2) -> (r3) -> (r4) -> (r2)
        while t not in store:
            rocks2 = cycle(rocks)
            store[t] = rocks2
            rocks = rocks2
            t = tup(rocks)
        
        # we've done total cycles so far
        total = len(store)
        # and there is a cyle of cycles of lengh l
        l = cycle_length(store, rocks)
        # so L more rounds of complete cycles of cycles
        L = (N - total) // l
        # and R more cycles to N
        R = N - (total + L*l)
        print(N, total, l, L, total + L*l, R)

        for i in range(R):
            rocks = cycle(rocks)

        pr(rocks)
        print(score(rocks))



