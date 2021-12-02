import sys

"""
Similar, to part 1, decided to keep the first run
check in the main loop and go with slicing on the window
to keep it general and easy-to-read rather than re-use
space with a collections.deque
"""

def count_depth_sum_increases(depths, window):
    increases = 0
    depth_window = []
    
    for depth in depths:

        if len(depth_window) != window:
            depth_window.append(int(depth))
        else:
            prev_depth_sum = sum(depth_window)
            depth_window = depth_window[1:]
            depth_window.append(int(depth))

            if sum(depth_window) > prev_depth_sum:
                increases = increases + 1

    return increases


if __name__ == '__main__':
    increases = count_depth_sum_increases(sys.stdin, 3)
    print("{}".format(increases))


