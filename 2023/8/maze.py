import sys

def dir(d):
    return 0 if d == 'L' else 1

def parse(line):
    key, paths = line.split("=")
    paths = paths.strip().split(",")
    
    return key.strip(), paths[0][1:], paths[1][1:len(paths[1])-1]



if __name__ == '__main__':
    
    maze = {}
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        steps = [dir(d) for d in list(lines[0].strip())]
        print(steps)
        for line in lines[2:]:
            k,l,r = parse(line)

            print(k,l,r)

            maze[k] = (l,r)
        
        start = 'AAA'
        count = 0
        dir = 0
        while start != 'ZZZ':
            start = maze[start][steps[dir]]
            count += 1
            dir = (dir + 1) % len(steps)
            print(start,count,dir)
        
        print()
        print(count)
        
        
