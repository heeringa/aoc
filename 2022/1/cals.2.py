import sys

    
def cals(calinput):
    top3 = [0, 0, 0]
    runningtotal = 0

    def replace(val):
        top3.pop()
        top3.append(val)
        top3.sort(reverse=True)
        
    
    for cal in calinput:
        cal = cal.strip()
        if cal == "":
            if runningtotal > top3[2]:
                replace(runningtotal)
            runningtotal = 0
        else:
            runningtotal += int(cal)

    if runningtotal > top3[2]:
        replace(runningtotal)
        
    return top3


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(sum(cals(file)))
