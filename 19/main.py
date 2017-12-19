"""
Day 19: A Series of Tubes
"""


def findstart(world):
    """
    Find start of the path
    """
    y = 0
    x = world[y].index('|')
    return (y, x)


def findpathletters(world):
    """
    Find letters visited while routing. Preserver valid order of the letters.
    """
    sty, stx = findstart(world)
    direction = 'down'
    actpos = world[sty][stx]
    letters = []
    steps = 0

    while actpos != ' ':
        steps += 1
        if direction == 'down':
            sty += 1
        elif direction == 'up':
            sty -= 1
        elif direction == 'right':
            stx += 1
        elif direction == 'left':
            stx -= 1
        else:
            raise Exception('Invalid direction')
        actpos = world[sty][stx]

        # letters
        if actpos.isalpha():
            letters.append(actpos)
        if actpos == '+':
            if direction == 'up' or direction == 'down':
                direction = 'left' if stx > 0 and world[sty][stx -
                                                             1] != ' ' else 'right'
            else:
                direction = 'up' if sty > 0 and world[sty -
                                                      1][stx] != ' ' else 'down'
    return ''.join(letters), steps


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').readlines()
    letters, steps = findpathletters(data)

    print('visited letters:', letters)
    print('made steps:', steps)


if __name__ == '__main__':
    main()
