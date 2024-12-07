import sys


if __name__ == '__main__':

    before = {}
    with open(sys.argv[1]) as fin:
        lines = fin.read()
        first, second = lines.split("\n\n")
        for line in first.split("\n"):
            l,r = line.split('|')
            l = int(l)
            r = int(r)
            before.setdefault(l,set()).add(r)
        
        good = []

        for line in second.split("\n"):
            pages = [int(i) for i in line.split(',')]
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
            if not err:
                good.append(pages)
        print(good)

        total = 0
        for lst in good:
            total += lst[len(lst)//2]
        print(total)
                    
                


