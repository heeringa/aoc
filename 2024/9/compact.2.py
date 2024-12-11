import sys


def spacetoblocks(diskmap):
    idx = 0
    s = []
    free = {i:[] for i in range(1,11)}
    block = 0
    for i in range(len(diskmap)):
        if i % 2 == 0:
            c = idx
            idx += 1
        else:
            c = None
            if int(diskmap[i]) > 0:
                free.get(int(diskmap[i])).append(block)
        s.extend(int(diskmap[i])*[c])
        block += int(diskmap[i])
    return (s,free)

def firstfree(free, length):
    first = None
    retlen= None
    for i in range(length,11):
        if len(free[i]) > 0:
            if first is None or free[i][0] < first:
                first = free[i][0]
                retlen = i
    return first,retlen

def update(blocks, free, newindex, oldindex, filelength, blocklength):
    for i in range(filelength):
        blocks[newindex+i] = blocks[oldindex+i]
        blocks[oldindex+i] = None
    free[blocklength].pop(0)
    if blocklength-filelength > 0:
        free[blocklength-filelength].append(newindex+filelength)
        free[blocklength-filelength].sort()
    
    


if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        diskmap = list(fin.read().strip())
        blocks,free = spacetoblocks(diskmap)

        print(blocks)
        print(free)

        idx = len(blocks)-1
        while idx > 0:
            filelength = 1            
            while idx > 0 and blocks[idx] == blocks[idx-1]:
                idx -= 1
                filelength += 1
            if blocks[idx] is not None:
                first, retlen = firstfree(free, filelength)
                #print("FIRST = {}, RETLEN={} IDX={}, VAL={}, LENGTH={}".format(first,retlen,idx,blocks[idx],filelength))                
                if first is not None and first < idx:
                    update(blocks, free, first, idx, filelength, retlen)
                #print(blocks)
                #print(free)
                #print()
            idx -= 1



        checksum = 0
        for i in range(len(blocks)):
            if blocks[i] is not None:
                checksum += i*int(blocks[i])
            else:
               pass
        print(checksum)
