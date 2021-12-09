import sys


def sub(str1, str2):
    l1 = list(str1)
    l2 = list(str2)
    for l in l2:
        if l in l1:
            l1.remove(l)
    return "".join(l1)
    
def zero_six_nine(length6, one, four):
    ret = {}
    for dig in length6:
        if len(sub(dig,four)) == 2:
            ret[9] = dig
            length6.remove(dig)
            break
    dig = length6[0]
    if len(sub(dig,one)) == 4:
        ret[0] = dig
        ret[6] = length6[1]
    else:
        ret[6] = dig
        ret[0] = length6[1]
    return ret

        
def two_three_five(length5, one, four):
    ret = {}
    for dig in length5:
        if (len(sub(dig,one)) == 3):
            ret[3] = dig
            length5.remove(dig)
            break
    if len(sub(length5[0],four)) == 2:
        ret[5] = length5[0]
        ret[2] = length5[1]
    else:
        ret[2] = length5[0]
        ret[5] = length5[1]        
    return ret


def parse(line):
    first,last = line.split('|')
    first = ["".join(sorted(s)) for s in first.strip().split()]
    last = ["".join(sorted(s)) for s in last.strip().split()]
    return (first, last)

if __name__ == '__main__':
    total = 0
    digits = {2:1, 4:4, 3:7, 7:8}
    for line in sys.stdin:
        first, last = parse(line)
        mapping = {}
        sixes = []
        fives = []
        for digit in first:
            if len(digit) in digits:
                mapping[digits[len(digit)]] = digit
            elif len(digit) == 6:
                sixes.append(digit)
            else:
                fives.append(digit)

        mapping.update(zero_six_nine(sixes, mapping[1], mapping[4]))
        mapping.update(two_three_five(fives, mapping[1], mapping[4]))
        
        inv = {}
        for k,v in mapping.items():
            inv[v] = k

        decode = []
        
        for digit in last:
            s = str(inv[digit])
            decode.append(s)


        total = total + int("".join(decode))

                 
    print(total)
