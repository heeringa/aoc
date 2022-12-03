import sys

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = [i for i in range(1,len(items)+1)]
pmap = { k:v for k,v in zip(items,priorities) }

def contents(sacks):
    total = 0
    for sack in sacks:
        stuff = list(sack.strip())
        l = len(stuff) // 2
        left = stuff[:l]
        right = stuff[l:]
        shared = set(left).intersection(set(right))
        shared = list(shared)[0]
        total += pmap[shared]
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as sacks:
        print(contents(sacks))
