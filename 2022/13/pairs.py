import sys
import json


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
        pairs = []
        l = None
        r = None
        for line in f:
            if line.strip() == '':
                l = None
                r = None
            elif l is None:
                l = json.loads(line.strip())
            else:
                pairs.append((l,json.loads(line.strip())))

        round = 1
        rounds = []
        for (l,r) in pairs:
            print("Considering L={} R={}".format(l,r))
            if compare(l,r):
                rounds.append(round)
            round += 1
            print()

        print(rounds)
        print(sum(rounds))
