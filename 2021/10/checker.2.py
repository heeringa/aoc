import sys


if __name__ == '__main__':

    pairs = {'{':'}', '(':')', '[':']', '<':'>'}
    scores = {')':1, ']':2, '}':3, '>':4}
    autoscores = []
    
    for line in sys.stdin:
        tokens = []
        corrupted = False
        for t in line.strip():
            # if we have an open character, slap it on the stack
            if t in pairs: 
                tokens.append(t)
            # otherwise we have a close character, so make sure we can pop
            elif len(tokens) != 0:
                t2 = tokens.pop()
                # popped character is open, so find corresponding close
                # and compare
                if (t != pairs[t2]):
                    corrupted = True
                    break

        if not corrupted:
            score = 0
            while len(tokens) != 0:
                score = 5*score + scores[pairs[tokens.pop()]]
            autoscores.append(score)
            
    autoscores.sort()
    print(autoscores[len(autoscores)//2])
