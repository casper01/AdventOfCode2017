"""
Day 25: The Halting Problem
"""


class TuringMachine:
    """
    Represents Turing Machine
    """
    INITSIZE = 50

    def __init__(self, startstate):
        self.state = startstate
        self.tape = [0] * TuringMachine.INITSIZE
        self.pos = int(len(self.tape) / 2)
        self.conditions = {}

    def addcondition(self, state, val, newval, movedir, newstate):
        """
        Add condition how the machine should move
        :param state: current machine state
        :param val: value in current position
        :param newval: new value in current pos
        :param movedir: how should the machine move (left or right)
        :param newstate: new state after moving
        """
        if state not in self.conditions:
            self.conditions[state] = {}
        self.conditions[state][val] = (newval, movedir, newstate)

    def _extendtapeleft(self):
        extension = [0] * TuringMachine.INITSIZE
        self.tape = extension + self.tape
        self.pos += len(extension)

    def _extendtaperight(self):
        extension = [0] * TuringMachine.INITSIZE
        self.tape = self.tape + extension

    def makestep(self):
        """
        Make single step
        """
        newval, movedir, newstate = self.conditions[self.state][self.tape[self.pos]]
        self.state = newstate
        self.tape[self.pos] = newval
        if movedir == 'right':
            self.pos += 1
        elif movedir == 'left':
            self.pos -= 1
        else:
            raise Exception('Invalid move')

        if self.pos < 0:
            self._extendtapeleft()
        elif self.pos >= len(self.tape):
            self._extendtaperight()

    def checksum(self):
        """
        Get checksum of current machine tape state
        """
        return sum(self.tape)


def getstartstate(data):
    """
    Get start state from input data
    :param data: input data divided to blocks
    :return: Char, representing starting state
    """
    state = data[0].split('\n')[0]
    state = state.split(' ')[-1]
    state = state[:-1]
    return state


def getsteps(data):
    """
    Get number of steps which machine should make from input data
    :param data: input data divided to blocks
    :return: integer, number of steps
    """
    steps = data[0].split('\n')[1]
    steps = steps.split(' ')[-2]
    return int(steps)


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').read().split('\n\n')
    startstate = getstartstate(data)
    steps = getsteps(data)
    machine = TuringMachine(startstate)

    for block in data[1:]:
        block = block.split('\n')
        state = block[0].split(' ')[-1][:-1]
        block.pop(0)
        for i in range(0, len(block), 4):
            val = int(block[i].split(' ')[-1][:-1])
            newval = int(block[i + 1].split(' ')[-1][:-1])
            movedir = block[i + 2].split(' ')[-1][:-1]
            newstate = block[i + 3].split(' ')[-1][:-1]
            machine.addcondition(state, val, newval, movedir, newstate)

    for iteration in range(steps):
        if iteration % 1000000 == 0:
            print('it = ', iteration)
        machine.makestep()
    print('checksum:', machine.checksum())


if __name__ == '__main__':
    main()
