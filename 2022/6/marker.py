import sys

def marker(line):

    def diff(s):
        return len(set(list(s))) == 4

    for i in range(4,len(line)):
        if diff(line[i-4:i]):
            return i

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(marker(f.readline()))
