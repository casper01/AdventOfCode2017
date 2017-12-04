"""
Day 3: Spiral Memory
"""


def getPerimeter(r):
    return 8 * abs(r)


def getNumber(r, d, h):
    # if r == 0:
    #     return 0
    if abs(r) < abs(d):
        return 0
    radius = abs(r)
    square_start = 1

    for i in range(0, radius):
        square_start += getPerimeter(i)

    number = square_start + radius

    if r < 0:
        number += 4 * radius

    if not h:
        number += 2 * radius

    number += d
    if number <= square_start:
        number = square_start + getPerimeter(radius)
    elif number > square_start + getPerimeter(radius):
        number = square_start + 1
    return number


def getRDH(number):
    number -= 1
    r = 0
    while number - getPerimeter(r) > 0:
        number -= getPerimeter(r)
        r += 1

    # compute d
    d = number - r
    while d not in range(-r, r + 1):
        d -= 2 * r

    # signs
    if number in range(2 * r + 1, 4 * r + 1) or number in range(6 * r + 1, 8 * r + 1):
        h = False
    else:
        h = True
    if number > 4 * r:
        r *= -1
    return r, d, h


def getCoords(number):
    number -= 1
    r = 0
    while number - getPerimeter(r) > 0:
        number -= getPerimeter(r)
        r += 1

    # compute d
    d = number - r
    while d not in range(-r, r + 1):
        d -= 2 * r

    if number <= 2 * r:
        x = r
        y = d
    elif number <= 4 * r:
        x = -d
        y = r
    elif number <= 6 * r:
        x = -r
        y = -d
    else:
        x = d
        y = -r
    return x, y


def main():
    data = open('input.txt', 'r').read()
    data = int(data)

    # part 1
    r, d, h = getRDH(data)
    ans = abs(r) + abs(d)
    print('part1: ', ans)

    #  part 2
    values = {}
    values[(0, 0)] = 1
    act_ind = 2
    while values[getCoords(act_ind-1)] < data:
        x, y = getCoords(act_ind)
        summ = 0
        for xx in range(-1, 2):
            for yy in range(-1, 2):
                if (x+xx, y+yy) in values:
                    summ += values[(x+xx, y+yy)]
        values[(x, y)] = summ
        act_ind += 1
    print('part2: ', values[getCoords(act_ind-1)])


def test():
    print('TESTY')
    for i in range(1, 27):
        print('-----------------------------------')
        print('num: ', i)
        r, d, h = getRDH(i)
        print('r = ', r)
        print('d = ', d)
        print('h = ', h)
        print('po powrocie: ', getNumber(r, d, h))
        print('-----------------------------------')


if __name__ == '__main__':
    main()
