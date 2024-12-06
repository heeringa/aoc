import sys


if __name__ == '__main__':

    def good(pages, before):
        err = False
        for i in range(len(pages)):
            for j in range(i+1,len(pages)):
                if pages[j] not in before.get(pages[i],set()):
                    err = True
                    break
                if err:
                    break
            if err:
                break
        return not err
        

    before = {}
    after = {}
    with open(sys.argv[1]) as fin:
        lines = fin.read()
        first, second = lines.split("\n\n")
        for line in first.split("\n"):
            l,r = line.split('|')
            l = int(l)
            r = int(r)
            before.setdefault(l,set()).add(r)
            after.setdefault(r,set()).add(l)
        
        bad = []

        for line in second.split("\n"):
            pages = [int(i) for i in line.split(',')]

            if not good(pages, before):
                bad.append(pages)
        
        for b in bad:
            print("BEFORE: {}: Good: {}".format(b, good(b,before)))
            for i in range(len(b)):
                for j in range(len(b)-2,-1,-1):
                    if b[j] in before.get(b[j+1],set()):
                        k = b[j+1]
                        b[j+1] = b[j]
                        b[j] = k
            print("AFTER: {}: Good: {}".format(b, good(b,before)))
            print()

        total = 0
        for lst in bad:
            total += lst[len(lst)//2]
        
        print(total)
                    
                


