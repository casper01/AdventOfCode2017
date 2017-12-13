"""
Day 13: Packet Scanners
"""


class Layer:
    def __init__(self, l_depth, l_range):
        self.l_depth = l_depth
        self.l_range = l_range
        self.pos = 0

    def move(self):
        self.pos += 1
        if self.pos == len(self.l_range):
            self.pos -= 2

    def caught(self, picosecond):
        return self.position(picosecond) == 0

    def cycle_time(self):
        return 2 * self.l_range - 2

    def position(self, picosecond):
        while picosecond - self.cycle_time() >= 0:
            picosecond -= self.cycle_time()
        return picosecond

    def serverity(self, picosecond):
        return self.l_depth * self.l_range if self.caught(picosecond) else 0


def main():
    data = open('input.txt', 'r').readlines()
    # data = ['0: 3',
    #         '1: 2',
    #         '4: 4',
    #         '6: 4']
    serverity = 0
    layers = []

    for info in data:
        l_depth, l_range = list(map(int, info.split(':')))
        layer = Layer(l_depth, l_range)
        serverity += layer.serverity(l_depth)
        layers.append(layer)

    print('serverity dla 0 = ', serverity)

    MAX = 10000000
    delay_arr = [True] * MAX
    for layer in layers:
        invalid_val = layer.cycle_time() - layer.l_depth
        while invalid_val < MAX:
            delay_arr[invalid_val] = False
            invalid_val += layer.cycle_time()
    if any(delay_arr):
        print('delay =', next(i for i, v in enumerate(delay_arr) if v))
    else:
        print('Brak wartosci mniejszych od', MAX)


if __name__ == '__main__':
    main()
