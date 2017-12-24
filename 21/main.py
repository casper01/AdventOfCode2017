"""
Day 21: Fractal Art
"""


class Grid:
    """
    Represents grid from the task
    """
    def __init__(self, strarr):
        self.grid = self._to2d(strarr)

    @staticmethod
    def frommatrix(matrix):
        """
        Create Grid object from matrix
        :param matrix: matrix from which grid will be created
        """
        grid = Grid('')
        grid.grid = matrix
        return grid

    def tostr(self):
        """
        Cast grid to valid string according to the task rules
        """
        return '/'.join([''.join(g) for g in self.grid])

    def printgrid(self):
        """
        Print grid to stdout
        """
        for row in self.grid:
            print(''.join(row))

    def _to2d(self, strgrid):
        """
        Cast string representation of grid to 2d array
        """
        return [list(s) for s in strgrid.split('/')]

    def flip(self, horizontally):
        """
        Perform flip operation on grid
        :param horizontally: If True, flip horizontally. Otherwise flip vertically
        """
        if horizontally:
            self.grid = [row[::-1] for row in self.grid]
        else:
            self.grid = self.grid[::-1]

    def rotateclockwise(self):
        """
        Rotate the grid by 90 degrees clockwise
        """
        self.grid = zip(*self.grid[::-1])
        self.grid = [list(row) for row in self.grid]

    @staticmethod
    def squarestogrid(squares, destwidth):
        """
        Make grid out of list of squares
        :param squares: List of squares
        :param destwidth: Width of resulting matrix
        :return: 2d matrix
        """
        sqperrow = int(destwidth / len(squares[0]))
        squarerows = [squares[i:i + sqperrow]
                      for i in range(0, len(squares), sqperrow)]

        finalans = []
        for squarerow in squarerows:
            ans = None
            for square in squarerow:
                if ans is None:
                    ans = square
                else:
                    ans = list(zip(ans, square))
                    ans = [t[0] + t[1] for t in ans]
            finalans.extend(ans)
        return finalans

    def tosquares(self, sqw):
        """
        Make list of squares out of grid
        :param sqw: Width of every output square
        :return: List of squares, each of equal width
        """
        squares = []
        for i in range(0, len(self.grid), sqw):
            for j in range(0, len(self.grid[i]), sqw):
                square = [[None for _ in range(sqw)] for _ in range(sqw)]
                for k in range(sqw):
                    for l in range(sqw):
                        square[k][l] = self.grid[i + k][j + l]
                squares.append(square)
        return squares

    def gethashescount(self):
        """
        Get number of hashes in grid
        """
        return sum([1 if el == '#' else 0 for row in self.grid for el in row])


class GridRule:
    """
    Represents one rule for grid
    """
    def __init__(self, strrule):
        condition, result = strrule.split(' => ')
        self._condition = Grid(condition)
        self._result = Grid(result)

    def condition(self):
        """
        Get condition of the rule
        """
        return self._condition

    def result(self):
        """
        Get result of the rule
        """
        return self._result


class GridRules:
    """
    Represents all rules for grid
    """
    def __init__(self):
        self.rules = {}

    def add(self, gridrule):
        """
        Add new rule (include all variations of it)
        :param gridrule: instance of GridRule object
        """
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().flip(False)
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().flip(True)
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().flip(False)
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().rotateclockwise()
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().flip(False)
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().flip(True)
        self.rules[gridrule.condition().tostr()] = gridrule.result()
        gridrule.condition().flip(False)
        self.rules[gridrule.condition().tostr()] = gridrule.result()

    def get(self, grid):
        """
        Get rule for specified grid
        :param grid: Grid object
        :return: Grid object - rule for specified grid
        """
        identifier = grid.tostr()
        rule = self.rules[identifier] if identifier in self.rules else None
        if rule is None:
            raise Exception('No rule for specified grid!')
        return rule


PART1_ITERATIONS = 5
PART2_ITERATIONS = 18


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').read().split('\n')
    startpattern = '.#./..#/###'
    startgrid = Grid(startpattern)

    gridrules = GridRules()
    for rule in data:
        gridrules.add(GridRule(rule))

    for i in range(PART2_ITERATIONS):
        print('i = ', i, '/', PART2_ITERATIONS)
        if i == PART1_ITERATIONS:
            part1hashes = startgrid.gethashescount()
        if len(startgrid.grid) % 2 == 0:
            squares = startgrid.tosquares(2)
            ressquares = [gridrules.get(Grid.frommatrix(square)).grid for square in squares]
            startgrid.grid = Grid.squarestogrid(ressquares, len(startgrid.grid) / 2 * 3)
        elif len(startgrid.grid) % 3 == 0:
            squares = startgrid.tosquares(3)
            ressquares = [gridrules.get(Grid.frommatrix(square)).grid for square in squares]
            startgrid.grid = Grid.squarestogrid(ressquares, len(startgrid.grid) / 3 * 4)
        else:
            raise Exception('Invalid grid dimensions')
    print('part1 hashes: ', part1hashes)
    print('part2 hashes: ', startgrid.gethashescount())


if __name__ == '__main__':
    main()
