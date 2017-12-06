"""
Day 5: A Maze of Twisty Trampolines, All Alike
"""


def main():
    data = open('input.txt', 'r').read().split()
    data = list(map(int, data))
    steps = 0
    act_ind = 0
    while act_ind < len(data):
        offset = data[act_ind]

        if offset >= 3:
            data[act_ind] -= 1
        else:
            data[act_ind] += 1

        act_ind += offset
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
