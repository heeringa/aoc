import sys


def spacetoblocks(diskmap):
    idx = 0
    s = []
    for i in range(len(diskmap)):
        if i % 2 == 0:
            c = idx
            idx += 1
        else:
            c = None
        s.extend(int(diskmap[i])*[c])
    print(s)
    return s

if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        diskmap = list(fin.read().strip())
        blocks = spacetoblocks(diskmap)
        print(blocks)
        blocks = list(blocks)
        i = 0
        j = len(blocks)-1
        while i < j:
            while blocks[i] is not None:
                i += 1
            while blocks[j] is None:
                j -= 1
            if (i<j):
                blocks[i] = blocks[j]
                blocks[j] = None
        print(blocks)
        checksum = 0
        for i in range(len(blocks)):
            if blocks[i] is not None:
                checksum += i*int(blocks[i])
            else:
               break
        print(checksum)
