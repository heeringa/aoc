import sys

def matches(s, arr):
    if len(s) == 0:
        if len(arr) == 0:
            return [""]
        else:
            return []
    
    # we can't match this character to an arrangement so
    # recrusively get the results, append '.' to them and return
    if s[0] == '.':
        results = matches(s[1:], arr)
        return ['.' + r for r in results]

    results = []    
    # we can choose to not match this ? and call it a '.'
    if s[0] == "?":
        results = ['.' + r for r in matches(s[1:], arr)]
    
    # if we have no more arrangements, we should return the results
    if len(arr) == 0:
        return results

    # now we're left with trying to match the next number
    # in our arrangement
    K = arr[0]
    
    # we don't have enough characters to match so we're out or luck
    # so nothing will work moving forward 
    if len(s) < K:
        return []
    
    # the first k characters of s need to be some combination of # and ?
    # so if we can't match, then return our results so far
    ss = s[:K]
    if any(ss[i] == '.' for i in range(K)):
        return results
    
    # we can match the first K characters of s, but we also need the k+1 
    # character to be a  . or ? (or the end of the string)
    # so that it's a true match
    if len(s) == K or (len(s) > K and s[K] in ['.', '?']):
        prefix = "#"*K
        if len(s) > K:
            prefix += '.'
        results2 = [prefix + r for r in matches(s[K+1:], arr[1:])]
        results.extend(results2)
        return results
    else:
        return results    

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        total = 0
        for line in f:
            s, arr = line.strip().split()
            arrs = [int(i) for i in arr.split(',')]
            print("S = {}\tArrs = {}".format(s, arrs))
            r = matches(s, arrs)
            print(r)
            print(len(r))
            print()
            total += len(r)
        print(total)