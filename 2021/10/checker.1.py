import sys


if __name__ == '__main__':

    pairs = {'{':'}', '(':')', '[':']', '<':'>'}
    scores = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    
    for line in sys.stdin:
        tokens = []
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
                    score += scores[t]
                    break
    print(score)
