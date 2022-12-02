import sys

# A = X = ROCK = 1
# B = Y = = PAPER = 2
# C = Z = SCISSORS = 3

points = {
    ('A','X') : 1+3,
    ('A','Y') : 2+6,
    ('A','Z') : 3+0,
    ('B','X') : 1+0,
    ('B','Y') : 2+3,
    ('B','Z') : 3+6,
    ('C','X') : 1+6,
    ('C','Y') : 2+0,
    ('C','Z') : 3+3
    }
    

def score(rounds):
    total = 0
    for round in rounds:
        round = round.split()
        u = round[0]
        v = round[1]
        total += points[(u,v)]
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as rounds:
        print(score(rounds))
