import sys

def parse_direction(direction):
    direction, distance = direction.split()
    if direction == 'forward':
        return (int(distance),0)
    elif direction == 'up':
        return (0,-int(distance))
    elif direction == 'down':
        return(0,int(distance))

def calculate_position(directions):
    position = (0,0)
    for direction in directions:
        h,v = parse_direction(direction)
        position = (position[0] + h, position[1] + v)
    return position


if __name__ == '__main__':
    final_position = calculate_position(sys.stdin)
    print("{}".format(final_position[0] * final_position[1]))



