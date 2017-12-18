"""
Day 18: Duet
"""


class Program:
    """
    Represents program that executes code
    """
    ACTIVE_STATUS = -1
    WAITING_STATUS = -2
    SENDING_STATUS = -3
    FINISHED_STATUS = -4

    def __init__(self, identifier, instructions):
        self.heap = {}
        self.snd = None
        self._status = Program.ACTIVE_STATUS
        self._id = identifier
        self._addvar('p', self._id)
        self.actinstr = 0
        self.instructions = instructions
        self.msgqueue = []

    def getid(self):
        """
        Get program ID
        """
        return self._id

    def addmsg(self, msg):
        """
        Add message to message queue
        """
        self.msgqueue.append(msg)
        if self._status == Program.WAITING_STATUS:
            self._status = Program.ACTIVE_STATUS
            self.actinstr -= 1

    def _getmsg(self):
        return self.msgqueue.pop(0) if self.msgqueue else None

    def status(self):
        """
        Get actual status of program. It can be:
        ACTIVE_STATUS, WAITING_STATUS, SENDING_STATUS, FINISHED_STATUS
        """
        return self._status

    def getsndval(self):
        """
        Get value that process want to send
        """
        var = self.snd
        self.snd = None
        self._status = Program.ACTIVE_STATUS
        return var

    def _snd(self, x):
        x = self.varvalue(x)
        self.snd = x
        self._status = Program.SENDING_STATUS

    def _rcv(self, x):
        msg = self._getmsg()
        if msg is None:
            self._status = Program.WAITING_STATUS
            return
        self._addvar(x, msg)

    def _set(self, x, y):
        y = self.varvalue(y)
        self.heap[x] = y

    def _add(self, x, y):
        y = self.varvalue(y)
        value = self.heap[x] if x in self.heap.keys() else 0
        value += y
        self.heap[x] = value

    def _mul(self, x, y):
        y = self.varvalue(y)
        value = self.heap[x] if x in self.heap.keys() else 0
        value *= y
        self.heap[x] = value

    def _mod(self, x, y):
        y = self.varvalue(y)
        value = self.heap[x] if x in self.heap.keys() else 0
        value %= y
        self.heap[x] = value

    def _jgz(self, x, y):
        x = self.varvalue(x)
        y = self.varvalue(y)
        if x <= 0:
            return 1
        return y

    def _isvar(self, s):
        return s.isalpha()

    def _addvar(self, name, intvalue):
        self.heap[name] = intvalue

    def _isint(self, s):
        return s.isnumeric()

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
            self._addvar(argname, int(argval))
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

            if command == 'snd':
                self._snd(args[0])
            elif command == 'set':
                self._set(args[0], args[1])
            elif command == 'add':
                self._add(args[0], args[1])
            elif command == 'mul':
                self._mul(args[0], args[1])
            elif command == 'mod':
                self._mod(args[0], args[1])
            elif command == 'rcv':
                self._rcv(args[0])
            elif command == 'jgz':
                step = self._jgz(args[0], args[1])
            self.actinstr += step
            # print('iteracja: ', self.actinstr)
        if self.actinstr == len(self.instructions):
            self._status = Program.FINISHED_STATUS
        return self._status


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').readlines()
    program0 = Program(0, data)
    program1 = Program(1, data)
    sent = 0

    while Program.ACTIVE_STATUS in [program0.status(), program1.status()]:
        while program0.status() == Program.ACTIVE_STATUS:
            status = program0.run()
            if status == Program.SENDING_STATUS:
                program1.addmsg(program0.getsndval())
        while program1.status() == Program.ACTIVE_STATUS:
            status = program1.run()
            if status == Program.SENDING_STATUS:
                program0.addmsg(program1.getsndval())
                sent += 1
    print(sent)


if __name__ == '__main__':
    main()
