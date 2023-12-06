import sys

def distances(timebound):
    return [(timebound - t)*t for t in range(timebound+1)]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        times = [int(time) for time in lines[0][len("Time:"):].split()]
        dists = [int(d) for d in lines[1][len("Distance:"):].split()]        
        
        prod = 1
        for time,dist in zip(times, dists):
            ds = distances(time)
            print(ds)
            prod *= len([d for d in ds if d > dist])

        print(prod)
