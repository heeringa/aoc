import sys

def hex2bin(hex):
    b = []
    for h in hex:
        b.extend([int(c) for c in bin(int(h,16))[2:].zfill(4)])
    return b

def bin2int(digits):
    s = "".join([str(i) for i in digits])
    return int(s,2)

def ver(digits, start):
    return bin2int(digits[start:start+3]), start+3

def typeid(digits, start):
    return ver(digits, start)

def literal(typeid):
    return typeid == 4

def readliteral(digits, start):
    ret = []
    while True:
        lead = digits[start]
        block = digits[start+1:start+5]
        ret.extend(block)
        start += 5
        if lead == 0:
            break
    return bin2int(ret), start


def readoperator(digits, start):
    ltid = digits[start]
    start += 1
    totalval = 0
    
    if ltid == 0:
        length = bin2int(digits[start:start+15])
        start += 15
        val,start = parse(digits, start, start+length)
        totalval += val
    else:
        length = bin2int(digits[start:start+11])
        start += 11
        for _ in range(length):
            val, start = parse(digits, start)
            totalval += val
    return totalval, start


def parse(digits, start, finish=None):
    vertotal = 0

    if finish is None:
        v,start = ver(digits,start)
        tid,start = typeid(digits,start)
        vertotal += v
        if literal(tid):
            lit, start = readliteral(digits, start)
        else:
            val, start = readoperator(digits, start)
            vertotal += val
    else:
        while start < finish:
            v,start = ver(digits,start)
            tid,start = typeid(digits,start)
            vertotal += v
            if literal(tid):
                lit, start = readliteral(digits, start)
            else:
                val, start = readoperator(digits, start)
                vertotal += val
    return vertotal, start
    
    
if __name__ == '__main__':
    digits = hex2bin(sys.stdin.readline().strip())
    start = 0
    vertotal = 0

    v,start = ver(digits,start)
    tid,start = typeid(digits,start)
    vertotal += v
    if literal(tid):
        lit, start = readliteral(digits, start)
    else:
        val, start = readoperator(digits, start)
        vertotal += val
    print(vertotal)
        
