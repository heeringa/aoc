import sys


def bin_to_int(bits):
    total = 0
    for b in bits:
        total = 2*total + b
    return total

def complement(bits):
    return [1-b for b in bits]
    
def parse(line):
    return [int(b) for b in list(line.strip())]

def common(lines):
    counts = None
    total = 0
    for line in lines:
        bits = parse(line)
        if counts is None:
            counts = bits
        else:
            counts = [x+y for x,y in zip(counts, bits)]
        total = total + 1

    def maj_bit(count):
        return 1 if count > total/2 else 0
    
    return [maj_bit(count) for count in counts]
        

if __name__ == '__main__':
    
    maj = common(sys.stdin)
    comp = complement(maj)
    print(maj)
    print(bin_to_int(maj))    
    print(comp)
    print(bin_to_int(comp)) 
    print(bin_to_int(maj) * bin_to_int(comp))
