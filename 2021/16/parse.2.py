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

def applyop(op, vals):
    if op == 0:
        return sum(vals)
    elif op == 1:
        prod = 1
        for v in vals:
            prod = v * prod
        return prod
    elif op == 2:
        return min(vals)
    elif op == 3:
        return max(vals)
    elif op == 5:
        return 1 if vals[0] > vals[1] else 0
    elif op == 6:
        return 1 if vals[0] < vals[1] else 0
    elif op == 7:
        return 1 if vals[0] == vals[1] else 0
    
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
    
    if ltid == 0:
        length = bin2int(digits[start:start+15])
        start += 15
        vals,start = parse(digits, start, start+length)
        return vals,start
    else:
        length = bin2int(digits[start:start+11])
        start += 11
        vals = []
        for _ in range(length):
            val, start = parse(digits, start)
            vals.append(val)
        return vals,start
    
def parse(digits, start, finish=None):
    if finish is None:
        v,start = ver(digits,start)
        tid,start = typeid(digits,start)
        if literal(tid):
            lit, start = readliteral(digits, start)
            return lit, start
        else:
            vals, start = readoperator(digits, start)
            return applyop(tid,vals), start
    else:
        vals = []
        while start < finish:
            v,start = ver(digits,start)
            tid,start = typeid(digits,start)
            if literal(tid):
                lit, start = readliteral(digits, start)
                vals.append(lit)
            else:
                vals2, start = readoperator(digits, start)
                vals.append(applyop(tid,vals2))
        return vals, start
        
    
if __name__ == '__main__':

    digits = hex2bin(sys.stdin.readline().strip())
    start = 0
    val, start = parse(digits, start)
    print(val)
        
