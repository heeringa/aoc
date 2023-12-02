import sys
import re


class Bag:

    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def __sub__(self, R, G, B):
        return Bag(self.R - R, self.G - G, self.B - B)

    def sat(self):
        return self.R >= 0 and self.G >= 0 and self.B >= 0
    

def parse_game(draw):
    R = 0
    G = 0
    B = 0
    for token in draw.split(','):
        num, color = token.split()
        num = int(num.strip())
        color = color.strip()
        if color == 'red':
            R += num
        elif color == 'green':
            G += num
        elif color == 'blue':
            B += num
    return R, G, B

def parse(line):
    REGEX = r'Game (\d+):\s+(.*)'
    game_id, draws = re.findall(REGEX, line)[0]
    #print("Draws = {}".format(draws))
    #print("Game ID = {}".format(game_id))    
    games = draws.split(';')
    return int(game_id), [parse_game(draw) for draw in games]


def power(line):
    game_id, draws = parse(line)
    print("Game ID = {} Draws = {}".format(game_id, draws))
    max_R = 0
    max_G = 0
    max_B = 0
    for R,G,B in draws:
        max_R = max(max_R, R)
        max_G = max(max_G, G)
        max_B = max(max_B, B)
    return max_R * max_G * max_B
    
if __name__ == '__main__':
    R = 12
    G = 13
    B = 14
    with open(sys.argv[1]) as f:
        total = 0
        for line in f:
            total += power(line)

        print(total)
