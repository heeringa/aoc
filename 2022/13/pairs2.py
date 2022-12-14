import sys
import json
from functools import cmp_to_key

def compare2(left, right):
    val = compare(left, right)
    if val is None:
        return 0
    elif val:
        return -1
    else:
        return 1

def compare(left, right):

    print("L = {}, R = {}".format(left,right))
    
    if type(left) == int and type(right) == int:
        print("L and R are both INTS")
        
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return None

    if type(left) == list and type(right) == list:
        print("L and R are both LISTS")
        
        if len(left) == 0 and len(right) == 0:
            return None
        elif len(left) == 0:
            return True
        elif len(right) == 0:
            return False
        else:
            val = compare(left[0], right[0])
            if val is None:
                return compare(left[1:], right[1:])
            else:
                return val

    if type(left) == int and type(right) == list:
        print("L is INT and R is LIST")
        return compare([left], right)
    
    if type(left) == list and type(right) == int:
        print("L is LIST and R is INT")        
        return compare(left, [right])
    
        
    

    
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        packets = [[2], [6]]
        for line in f:
            if line.strip() != '':
                packets.append(json.loads(line.strip()))

        packets.sort(key=cmp_to_key(compare2))

        for packet in packets:
            print(packet)


        two = packets.index([2]) +1
        six = packets.index([6]) +1

        print(two)
        print(six)

        print(two*six)
        
