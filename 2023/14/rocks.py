import sys


def transpose(X):
    return [list(x) for x in zip(*X)]


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

def score(rocks):

    def score_row(row, val):
        return sum(val for r in row if r == 'O')

    return sum(score_row(row, val) for row, val in zip(rocks, range(len(rocks), 0, -1)))


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        rocks = [list(line.strip()) for line in f]
        rocks = transpose(rocks)
        rocks = west(rocks)
        rocks = transpose(rocks)

        for row in rocks:
            print(''.join(row))

        print(score(rocks))                   


