import sys


class Hand:

    _order = ['A', 'K', 'Q', 'T', '9', '8', 
              '7', '6', '5', '4', '3', '2', 'J']
    
    def __init__(self, cards, bid):
        self.cards = list(cards)
        self.bid = int(bid)

    def __lt__(self, other):
        """ Returns True if """
        c1 = self._classify()
        c2 = other._classify()
        if c1 < c2:
            return True
        elif c1 > c2:
            return False
        else:
            for i in range(len(self.cards)):
                o1 = Hand._order.index(self.cards[i])
                o2 = Hand._order.index(other.cards[i])
                if o1 < o2:
                    return True
                elif o1 > o2:
                    return False
        return False
        

    def __str__(self):
        return ''.join(self.cards) + ' ' + str(self.bid)

    def _classify(self):
        counts = {}
        for card in self.cards:
            counts[card] = counts.get(card, 0) + 1
        
        if 'J' in counts:
            jcount = counts['J']
            # if the joker is present, we should replace all jokers
            # with the card that appears the most
            del counts['J']
            maxcard = None
            maxcount = 0
            for card, count in counts.items():
                if count > maxcount:
                    maxcard = card
                    maxcount = count
            
            # all cards were jokers so it's 5 of a kind
            if maxcard is None:
                return 0
            else:
                counts[maxcard] += jcount
        
        vals = sorted(counts.values())
        if vals[0] == 5:
            return 0
        if vals[0] == 1 and vals[1] == 4:
            return 1
        if vals[0] == 2 and vals[1] == 3:
            return 2
        if vals[0] == 1 and vals[1] == 1 and vals[2] == 3:
            return 3
        if vals[0] == 1 and vals[1] == 2 and vals[2] == 2:
            return 4
        if vals[3] == 2:
            return 5
        return 6
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        hands = [Hand(*line.split()) for line in f]
        hands.sort()
        total = 0
        for i,hand in enumerate(hands):
            total += hand.bid * (len(hands) - i)
        print(total)
            

