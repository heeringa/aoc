import sys
    
def h(s, val):
    print("Calling Hash with {} and {}".format(s, val))
    val += ord(s)
    val *= 17
    val %= 256
    return val

def score(map):
    total = 0
    for k,v in map.items():
        for i, (label, scr) in enumerate(v):
            s = (1+k) * (1+i) * scr
            print("Box {} with Slot {} and score {} has value {}".format(k,i,scr,s))
            total += s
    return total


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        codes = f.read().strip()
        codes = codes.split(',')
        print(codes)
        total = 0
        map = {}
        for instruction in codes:
            hashval = 0
            val = None
            label = None
            op = None
            if instruction[-1] == '-':
                label = instruction[0:len(instruction)-1]
                op = '-'
            else:
                label, val = instruction.split("=")
                op = "="
                val = int(val)
            for c in label:
                hashval = h(c, hashval)
            print("Value of {} is {} with op = {}".format(label, hashval, op))

            if op == '-' and hashval in map:
                lst = map[hashval]
                map[hashval] = [(x,y) for x,y in lst if x != label]
            if op == '=':
                if hashval in map:
                    lst = map[hashval]
                    found = False
                    i = None
                    for j, (x,y) in enumerate(lst):
                        if x == label:
                            found = True
                            i = j
                            break
                    if not found:
                        lst.append((label,val))
                    else:
                        lst[j] = (label, val)
                else:
                    map[hashval] = [(label, val)]
            
            print(map)
            print(score(map))
