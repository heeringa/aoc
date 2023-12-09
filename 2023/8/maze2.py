import sys
import functools
import operator

def prod(nums):
    return functools.reduce(operator.mul, nums, 1)

def dir(d):
    return 0 if d == 'L' else 1

def parse(line):
    key, paths = line.split("=")
    paths = paths.strip().split(",")
    
    return key.strip(), paths[0][1:], paths[1][1:len(paths[1])-1]

def finished(states):
    return all(s.endswith('Z') for s in states)



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
        
        states = [k for k in maze.keys() if k.endswith('A')]
        print(states)

        def determine_phase(state):
            count = 0
            dir = 0
            while not state.endswith('Z'):
                state = maze[state][steps[dir]]
                count += 1
                dir = (dir + 1) % len(steps)
            return count // len(steps)
        
        phases = [determine_phase(s) for s in states]
        print(phases)
        print(prod(phases)*len(steps))
        
