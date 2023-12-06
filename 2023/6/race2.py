import sys

def count_times(timebound, distance):
    count = 0
    for t in range(timebound+1):
        if (timebound - t) * t > distance:
            count += 1
    return count

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        time = int("".join(lines[0][len("Time:"):].split()))
        dist = int("".join(lines[1][len("Distance:"):].split()))

        print(time)
        print(count_times(time, dist))

