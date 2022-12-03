import sys

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = [i for i in range(1,len(items)+1)]
pmap = { k:v for k,v in zip(items,priorities) }

def contents(sacks):
    total = 0
    i = 0
    while i < len(sacks):
        triples = []
        for j in range(3):
            triples.append(set(sacks[i+j].strip()))
        i += 3
        shared = triples[0].intersection(triples[1],triples[2])
        shared = list(shared)[0]
        total += pmap[shared]
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as sacks:
        print(contents(list(sacks)))
