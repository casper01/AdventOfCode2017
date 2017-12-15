"""
Day 13: Packet Scanners
"""


class Layer:
    """
    Represents layer of firewall
    """

    def __init__(self, l_depth, l_range):
        self.l_depth = l_depth
        self.l_range = l_range
        self.pos = 0

    def caught(self, picosecond):
        """
        Check if security scanner caught us in time picosecond
        """
        return self.position(picosecond) == 0

    def cycle_time(self):
        """
        Time of full cycle of layer
        """
        return 2 * self.l_range - 2

    def position(self, picosecond):
        """
        Position of security scanner in layer in time picosecond
        """
        while picosecond - self.cycle_time() >= 0:
            picosecond -= self.cycle_time()
        return picosecond

    def serverity(self, picosecond):
        """
        Compute serverity of layer
        """
        return self.l_depth * self.l_range if self.caught(picosecond) else 0

MAXIMUM = 10000000

def main():
    """
    Main function
    """
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

    delay_arr = [True] * MAXIMUM
    for layer in layers:
        invalid_val = layer.cycle_time() - layer.l_depth
        while invalid_val < MAXIMUM:
            delay_arr[invalid_val] = False
            invalid_val += layer.cycle_time()
    try:
        print('delay =', next(i for i, v in enumerate(delay_arr) if v))
    except StopIteration:
        print('Brak wartosci mniejszych od', MAXIMUM)


if __name__ == '__main__':
    main()
