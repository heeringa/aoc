import sys

def parse_direction(direction, aim):
    direction, val = direction.split()
    if direction == 'forward':
        return (int(val), int(val)*aim, 0)
    elif direction == 'up':
        return (0, 0, -int(val))
    elif direction == 'down':
        return(0, 0, int(val))

def calculate_position(directions):
    position = (0,0,0)
    for direction in directions:
        h,v,a = parse_direction(direction, position[2])
        position = (position[0] + h, position[1] + v, position[2] + a)
    return position


if __name__ == '__main__':
    final_position = calculate_position(sys.stdin)
    print("{}".format(final_position[0] * final_position[1]))
