"""
Day 15: Dueling Generators
"""

GENERATOR1FACTOR = 16807
GENERATOR2FACTOR = 48271
GENERATOR_MODULO = 2147483647
PHASE1ITERATIONS = int(40e6)
PHASE2ITERATIONS = int(5e6)


class Generator:
    """
    Generates numbers according to the task
    """
    LOWEST16 = int('1111111111111111', 2)

    @staticmethod
    def judge(num1, num2):
        """
        Compares 2 numbers and checks if 16 lowest bits are equal
        :return: true if 16 lowest bits are equal, otherwise false
        """
        num1 = num1 ^ num2
        return num1 & Generator.LOWEST16 == 0

    def __init__(self, startnumber, factor, modulo):
        self.num = startnumber
        self.factor = factor
        self.modulo = modulo

    def generate(self):
        """
        Generates numbers according to the task
        :return: generated number
        """
        self.num *= self.factor
        self.num %= self.modulo
        return self.num


class DivisibleNumbersGenerator(Generator):
    """
    Represents number generator
    all the generated numbers must be divisible by specified factor
    """

    def __init__(self, startnumber, factor, modulo, divisor):
        super(DivisibleNumbersGenerator, self).__init__(
            startnumber, factor, modulo)
        self.divisor = divisor

    def generate(self):
        while super(DivisibleNumbersGenerator, self).generate() % self.divisor != 0:
            pass
        return self.num


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').readlines()
    g1start = int(data[0].split()[-1])
    g2start = int(data[1].split()[-1])
    # g1start = 65
    # g2start = 8921

    ## PHASE 1
    gen1 = Generator(g1start, GENERATOR1FACTOR, GENERATOR_MODULO)
    gen2 = Generator(g2start, GENERATOR2FACTOR, GENERATOR_MODULO)
    match = 0
    percent = int(PHASE1ITERATIONS / 100)
    for i in range(PHASE1ITERATIONS):
        if (i + 1) % percent == 0:
            print('phase1: {}%'.format(int((i + 1) / percent)))
        num1 = gen1.generate()
        num2 = gen2.generate()
        match += 1 if Generator.judge(num1, num2) else 0
    print('Phase1 solution:', match)

    # PHASE 2
    gen1 = DivisibleNumbersGenerator(
        g1start, GENERATOR1FACTOR, GENERATOR_MODULO, 4)
    gen2 = DivisibleNumbersGenerator(
        g2start, GENERATOR2FACTOR, GENERATOR_MODULO, 8)
    match = 0
    percent = int(PHASE2ITERATIONS / 100)
    for i in range(PHASE2ITERATIONS):
        if (i + 1) % percent == 0:
            print('phase2: {}%'.format(int((i + 1) / percent)))
        num1 = gen1.generate()
        num2 = gen2.generate()
        match += 1 if DivisibleNumbersGenerator.judge(num1, num2) else 0
    print('match:', match)


if __name__ == '__main__':
    main()
