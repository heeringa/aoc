import sys

def nextday(counts):
    newcounts = [0]*9
    for i, count in enumerate(counts):
        if i == 0:
            newcounts[8] = count
            newcounts[6] = count
        else:
            newcounts[i-1] = newcounts[i-1] + count
    return newcounts

if __name__ == '__main__':
    counts = [0]*9
    for fish in sys.stdin.readline().split(','):
        fish = int(fish)
        counts[fish] = counts[fish] + 1
    
    days = 256
    for _ in range(days):
        counts = nextday(counts)
    print(sum(counts))
        
