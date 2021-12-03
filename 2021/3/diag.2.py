import sys

def filter_by_bit_at_pos(lst, bit, pos):
    return [l for l in lst if l[pos] == bit]

def most_common(lst, pos):
    return 1 if (sum(l[pos] for l in lst) >= len(lst) / 2) else 0

def least_common(lst, pos):
    return 0 if (sum(l[pos] for l in lst) >= len(lst) / 2) else 1

def O2(lst, pos):
    if len(lst) > 1:
        most = most_common(lst, pos)
        ret = filter_by_bit_at_pos(lst, most, pos)
        return O2(ret, pos+1)
    else:
        return lst[0]

def CO2(lst, pos):
    if len(lst) > 1:
        least = least_common(lst, pos)
        ret = filter_by_bit_at_pos(lst, least, pos)
        return CO2(ret, pos+1)
    else:
        return lst[0]    
    
def bin_to_int(bits):
    total = 0
    for b in bits:
        total = 2*total + b
    return total

def complement(bits):
    return [1-b for b in bits]
    
def parse(line):
    return [int(b) for b in list(line.strip())]

if __name__ == '__main__':

    input = [parse(line) for line in sys.stdin]
    oxy = O2(input,0)
    carb = CO2(input,0)
    print(bin_to_int(oxy)*bin_to_int(carb))    

    
