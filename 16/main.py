"""
Day 16: Permutation Promenade
"""

MAXCYCLE = int(1e9)


class DancingString:
    """
    Allows to perform dancing operations on string.
    Possible operations:
    - spin: sX
    - exchange: xA/B
    - partner: pA/B
    """

    def __init__(self):
        self.seq = []
        firstchar = 'a'
        lastchar = 'p'
        for i in range(ord(firstchar), ord(lastchar) + 1):
            self.seq.append(chr(i))

    @staticmethod
    def findcycle(actionlist, maxcycle):
        """
        Find how many times perform list of operations to return to original state
        :param actionlist: list of proper action string
        :return: number of operation
        """
        dstring = DancingString()
        originalseq = dstring.seq[:]
        i = 0
        for i in range(maxcycle):
            dstring.action(actionlist)
            if dstring.seq == originalseq:
                break
        return i + 1

    def _spin(self, endnum):
        self.seq = self.seq[-endnum:] + self.seq[:-endnum]

    def _exchange(self, aind, bind):
        self.seq[aind], self.seq[bind] = self.seq[bind], self.seq[aind]

    def _partner(self, achar, bchar):
        aind = self.seq.index(achar)
        bind = self.seq.index(bchar)
        self.seq[aind], self.seq[bind] = self.seq[bind], self.seq[aind]

    def _action(self, actionstr):
        if len(actionstr) <= 1:
            raise Exception('Invalid string')
        actiontype = actionstr[0]
        actionstr = actionstr[1:]
        if actiontype == 's':
            endnum = int(actionstr)
            self._spin(endnum)
        elif actiontype == 'x':
            aind, bind = map(int, actionstr.split('/'))
            self._exchange(aind, bind)
        elif actiontype == 'p':
            achar, bchar = actionstr.split('/')
            self._partner(achar, bchar)
        else:
            raise Exception('Invalid action type')

    def action(self, actionlist):
        """
        Perform dancing actions on sequence
        :param actionlist: list of dacing actions to perform on string
        """
        for actionstr in actionlist:
            self._action(actionstr)

    def getstring(self):
        """
        Return sequence of dancing chars as string
        :return: String - dancing sequence
        """
        return ''.join(self.seq)


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').read().split(',')

    dancingstring = DancingString()
    dancingstring.action(data)
    print('Part 1: ', dancingstring.getstring())

    times = MAXCYCLE % DancingString.findcycle(data, MAXCYCLE)
    dancingstring = DancingString()
    for _ in range(times):
        dancingstring.action(data)
    print('Part 2: ', dancingstring.getstring())


if __name__ == '__main__':
    main()
