import sys

def cals(calinput):
    maxtotal = -1
    runningtotal = 0
    for cal in calinput:
        cal = cal.strip()
        if cal == "":
            maxtotal = max(maxtotal, runningtotal)
            runningtotal = 0
        else:
            runningtotal += int(cal)
    maxtotal = max(maxtotal, runningtotal)
    return maxtotal


if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        print(cals(file))
