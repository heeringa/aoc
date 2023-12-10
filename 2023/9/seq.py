import sys

def diff_list(l):
    return [l[i+1] - l[i] for i in range(len(l)-1)]

def all_zeroes(l):
    return all([x == 0 for x in l])

def next_val(rows):
    next = 0
    for row in rows:
        print("NEXT: {} ROW: {}".format(next, row))
        next = row[-1] + next
    print("Final Next = {}".format(next))
    return next

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        total = 0
        for line in f:
            print(line)
            line = list([int(l) for l in line.split()])
            rows = []
            while not all_zeroes(line):
                rows.append(line)
                line = diff_list(line)
            total += next_val([row for row in reversed(rows)])
        print(total)