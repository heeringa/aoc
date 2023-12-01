import sys

WORDS = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def parse_line(line):
    print("Line = {}".format(line))
    first = None
    last = None
    i = 0
    L = len(line)
    while i < L:
        for word in WORDS.keys():
            if first is None and (line[i:].startswith(word) or line[i] == WORDS[word]):
                print("Line[{}:] = {} starts with {} or {}".format(i, line[i:], word, WORDS[word]))
                first = int(WORDS[word])
            if last is None and (line[L-i-1:].startswith(word) or line[L-i-1] == WORDS[word]):
                print("Line[{}:] = {} starts with {} or {}".format(L-i-1, line[L-i-1:], word, WORDS[word]))
                last = int(WORDS[word])
            if first is not None and last is not None:
                break
        if first is not None and last is not None:
            print("first = {}, last = {}".format(first, last))
            return first*10 + last
        i += 1
    print("first = {}, last = {}".format(first, last))
    return first*10 + last

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        total = 0
        for line in f:
            total += parse_line(line)
        print(total)
