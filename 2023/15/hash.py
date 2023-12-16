import sys
    
def h(s, val):
    print("Calling Hash with {} and {}".format(s, val))
    val += ord(s)
    val *= 17
    val %= 256
    return val



if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        codes = f.read().strip()
        codes = codes.split(',')
        print(codes)
        total = 0
        for code in codes:
            val = 0
            for c in code:
                print(c)
                val = h(c, val)
            print("Value of {} is {}".format(code, val))
            total += val
        print(total)
