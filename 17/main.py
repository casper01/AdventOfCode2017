"""
Day 17: Spinlock
"""

SEQ1LEN = 2018
SEQ2LEN = 50000000


def main():
    """
    Main function
    """
    forward = int(open('input.txt', 'r').read())

    # phase 1: construct sequence
    seq = [0]
    actind = 0
    for i in range(1, SEQ1LEN):
        actind = ((actind + forward) % len(seq)) + 1
        if actind == len(seq):
            seq.append(i)
        else:
            seq.insert(actind, i)
    print('Part 1: ', seq[actind + 1])

    # phase 2: monitor value after 0
    actind = 0
    actlen = 1
    val = 0
    for i in range(1, SEQ2LEN):
        actind = ((actind + forward) % actlen) + 1
        if actind == 1:
            val = i
        actlen += 1
    print('Part 2: ', val)


if __name__ == '__main__':
    main()
