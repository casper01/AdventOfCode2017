"""
Day 11: Hex Ed
"""

def dist_to_middle(x, y):
    steps = 0
    if x < 0 and y < 0:
        x *= -1
        y *= -1
    if x >= 0 and y >= 0:
        steps = max(x, y)
        return steps

    # case: different signs
    return abs(x) + abs(y)


def main():
    data = open('input.txt', 'r').read()
    # data = 'se,sw,se,sw,sw'
    
    dirs = data.split(',')
    x = 0
    y = 0
    max_dist = 0
    for direction in dirs:
        if direction == 'n':
            x += 1
            y += 1
        elif direction == 's':
            x -= 1
            y -= 1
        elif direction == 'nw':
            y += 1
        elif direction == 'se':
            y -= 1
        elif direction == 'ne':
            x += 1
        elif direction == 'sw':
            x -= 1
        max_dist = max(max_dist, dist_to_middle(x, y))
    dist = dist_to_middle(x, y)
    print(dist)
    print(max_dist)


if __name__ == '__main__':
    main()
