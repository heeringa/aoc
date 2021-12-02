import sys

"""
Decided to muddy the main loop with the 
first run check for the sake of keeping 
it streaming and not having an ugly one-off 
bit of code that grabs the first item and 
still gracefully handles the null stream
"""

def count_depth_increases(depths):
    increases = 0
    last_depth = None
    
    for depth in depths:

        depth = int(depth)

        if last_depth is None:
            last_depth = depth
            
        if depth > last_depth:
            increases = increases + 1
            
        last_depth = depth
    
    return increases


if __name__ == '__main__':
    increases = count_depth_increases(sys.stdin)
    print("{}".format(increases))


