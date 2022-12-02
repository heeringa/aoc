import sys

# A = X = ROCK = 1
# B = Y = = PAPER = 2
# C = Z = SCISSORS = 3

# X = LOSE
# Y = DRAW
# Z = WIN

points = {
    ('A','X') : 0+3,
    ('A','Y') : 3+1,
    ('A','Z') : 6+2,
    ('B','X') : 0+1,
    ('B','Y') : 3+2,
    ('B','Z') : 6+3,
    ('C','X') : 0+2,
    ('C','Y') : 3+3,
    ('C','Z') : 6+1
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
