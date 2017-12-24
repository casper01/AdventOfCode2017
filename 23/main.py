"""
Day 23: Coprocessor Conflagration
"""


class Program:
    """
    Represents program that executes code
    """
    ACTIVE_STATUS = -1
    FINISHED_STATUS = -4

    def __init__(self, identifier, instructions):
        self.heap = {}
        self._status = Program.ACTIVE_STATUS
        self._id = identifier
        self.actinstr = 0
        self.instructions = instructions
        self.mulcount = 0

    def getid(self):
        """
        Get program ID
        """
        return self._id

    def status(self):
        """
        Get actual status of program. It can be:
        ACTIVE_STATUS, WAITING_STATUS, SENDING_STATUS, FINISHED_STATUS
        """
        return self._status

    def _set(self, x, y):
        y = self.varvalue(y)
        self.heap[x] = y

    def _sub(self, x, y):
        y = self.varvalue(y)
        value = self.heap[x] if x in self.heap.keys() else 0
        value -= y
        self.heap[x] = value

    def _mul(self, x, y):
        y = self.varvalue(y)
        value = self.heap[x] if x in self.heap.keys() else 0
        value *= y
        self.heap[x] = value

    def _jgz(self, x, y):
        x = self.varvalue(x)
        y = self.varvalue(y)
        if x <= 0:
            return 1
        return y

    def _jnz(self, x, y):
        x = self.varvalue(x)
        y = self.varvalue(y)
        if x == 0:
            return 1
        return y

    def _isvar(self, string):
        return string.isalpha()

    def setvar(self, name, intvalue):
        """
        Set variable to specified value
        :param name: name of the variable
        :param intvalue: value of the variable
        """
        self.heap[name] = intvalue

    def _isint(self, string):
        return string.isnumeric()

    def varvalue(self, varname):
        """
        Get value of specified variable
        """
        return self.heap[varname] if varname in self.heap.keys() else 0

    # def recovered(self):
    #     return self._recovered

    def _parseinstr(self, instr):
        instr = instr.split()
        command = instr[0]
        tmpind = 0
        args = []
        for i in range(1, len(instr)):
            argval = instr[i]
            if self._isvar(argval):
                args.append(argval)
                continue

            argname = 'tmp' + str(tmpind)
            tmpind += 1
            self.setvar(argname, int(argval))
            args.append(argname)
        return command, args

    def run(self):
        """
        Run program code
        """
        self._status = Program.ACTIVE_STATUS
        while 0 <= self.actinstr < len(self.instructions) and self._status == Program.ACTIVE_STATUS:
            step = 1
            command, args = self._parseinstr(self.instructions[self.actinstr])

            if command == 'set':
                self._set(args[0], args[1])
            elif command == 'sub':
                self._sub(args[0], args[1])
            elif command == 'mul':
                self.mulcount += 1
                self._mul(args[0], args[1])
            elif command == 'jgz':
                step = self._jgz(args[0], args[1])
            elif command == 'jnz':
                step = self._jnz(args[0], args[1])
            else:
                raise Exception('Invalid instruction')
            self.actinstr += step
        if self.actinstr == len(self.instructions):
            self._status = Program.FINISHED_STATUS
        return self._status


def codeinpython(a=1, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
    """
    Input code in assembler rewrited to python
    """
    b = 108400
    c = 125400

    # check if every 17-th number from b to c is prime - count not prime numbers
    while True:
        f = 1
        d = 2
        label_e = True
        # check if b has got any factors (act factor checked: d)
        while label_e:
            e = 2
            label_d = True
            # check if d is factor of b (check if d * e == b)
            while label_d:
                if (d * e) - b == 0:
                    f = 0
                e += 1
                label_d = e - b != 0
            d += 1
            label_e = d - b != 0
        # if b has got any factor, increment counter
        if f == 0:
            h += 1
        if b - c == 0:
            return h
        b += 17


def optimizedcodeinpython():
    """
    Optimized version of input code
    """
    fromnum = 108400
    tonum = 125400
    step = 17
    sieve = findprimes(tonum)
    return sum(
        [1 if not sieve[num] else 0 for num in range(fromnum, tonum + 1, step)])


def findprimes(maxprime):
    """
    Use algorithm sieve of Eratosthenes to find prime numbers
    in range [2; maxprime].
    :return: Array of bools. sieve[n] is true if and only if n is prime number
    """
    sieve = [True] * (maxprime + 1)
    for i in range(2, maxprime + 1):
        if not sieve[i]:
            continue
        for j in range(2 * i, maxprime + 1, i):
            sieve[j] = False
    return sieve


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').readlines()

    program = Program(0, data)
    for char in range(ord('a'), ord('h') + 1):
        program.setvar(chr(char), 0)
    # program.setvar('a', 1)

    program.run()
    print('number of multiplications:', program.mulcount)
    h_register = optimizedcodeinpython()
    print('register h value:', h_register)


if __name__ == '__main__':
    main()
