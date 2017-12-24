"""
Day 22: Sporifica Virus
"""

import math

ITERATIONS = 10000000

CLEAN_NODE = '.'
INFECTED_NODE = '#'
WEAKENED_NODE = 'W'
FLAGGED_NODE = 'F'


def creategrid(data):
    """
    Create 2d grid of input data
    :param data: input data from the task
    :return: valid 2d array representing grid computing cluster
    """
    data = data.split('\n')
    grid = []
    for line in data:
        grid.append(list(line))
    return grid


class Virus:
    """
    Represents virus from the task
    """
    DIR_UP = 0
    DIR_RIGHT = 1
    DIR_DOWN = 2
    DIR_LEFT = 3

    def __init__(self, grid):
        self.grid = grid
        self.madeinfections = 0
        mid_i = math.floor(len(grid) / 2)
        mid_j = math.floor(len(grid[0]) / 2)
        self.pos = (mid_i, mid_j)
        self.dir = Virus.DIR_UP

    def _increasegrid(self, direction):
        """
        Increase grid in one of the directions
        :param direction: one of those: DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT
        """
        height = len(self.grid)
        width = len(self.grid[0])
        if direction == Virus.DIR_UP:
            newrows = [list(CLEAN_NODE * width) for _ in range(height)]
            self.grid = newrows + self.grid
            self.pos = (self.pos[0] + height, self.pos[1])
        elif direction == Virus.DIR_DOWN:
            newrows = [list(CLEAN_NODE * width) for _ in range(height)]
            self.grid.extend(newrows)
        elif direction == Virus.DIR_LEFT:
            newcols = list(CLEAN_NODE * width)
            for i, _ in enumerate(self.grid):
                self.grid[i] = newcols + self.grid[i]
            self.pos = (self.pos[0], self.pos[1] + width)
        elif direction == Virus.DIR_RIGHT:
            newcols = (CLEAN_NODE * width)
            for row in self.grid:
                row.extend(newcols)

    def _turn(self):
        """
        Change direction of moving
        """
        i, j = self.pos
        if self.grid[i][j] == INFECTED_NODE:
            factor = 1
        elif self.grid[i][j] == CLEAN_NODE:
            factor = -1
        elif self.grid[i][j] == WEAKENED_NODE:
            factor = 0
        elif self.grid[i][j] == FLAGGED_NODE:
            factor = 2
        else:
            raise Exception('Invalid ndoe type in grid')

        self.dir = (self.dir + factor) % 4

    def _updatecurrnodeinfection(self):
        """
        Updates infrection of current node
        """
        i, j = self.pos
        if self.grid[i][j] == CLEAN_NODE:
            self.grid[i][j] = WEAKENED_NODE
        elif self.grid[i][j] == WEAKENED_NODE:
            self.grid[i][j] = INFECTED_NODE
            self.madeinfections += 1
        elif self.grid[i][j] == INFECTED_NODE:
            self.grid[i][j] = FLAGGED_NODE
        elif self.grid[i][j] == FLAGGED_NODE:
            self.grid[i][j] = CLEAN_NODE
        else:
            raise Exception('Invalid flag of node in grid')

    def _move(self):
        """
        Makes one step in direction specified in self.dir
        """
        if self.dir == Virus.DIR_UP:
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.dir == Virus.DIR_DOWN:
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.dir == Virus.DIR_RIGHT:
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.dir == Virus.DIR_LEFT:
            self.pos = (self.pos[0], self.pos[1] - 1)
        else:
            raise Exception('Invalid move')

        if self.pos[0] < 0:
            self._increasegrid(Virus.DIR_UP)
        if self.pos[1] < 0:
            self._increasegrid(Virus.DIR_LEFT)
        if self.pos[0] >= len(self.grid):
            self._increasegrid(Virus.DIR_DOWN)
        if self.pos[1] >= len(self.grid[0]):
            self._increasegrid(Virus.DIR_RIGHT)

        if len(self.grid[0]) != len(self.grid[self.pos[0]]):
            print('anomalia')

    def makeburst(self):
        """
        Make one iteration of virus movement.
        It turns to proper side, updates current node
        and moves virus to the other node
        """
        self._turn()
        self._updatecurrnodeinfection()
        self._move()


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').read()
    grid = creategrid(data)
    virus = Virus(grid)

    for iteration in range(ITERATIONS):
        if (iteration+1) % (ITERATIONS/10) == 0:
            print('it = ', iteration+1, '/', ITERATIONS)
        virus.makeburst()
    print('made infections: ', virus.madeinfections)


if __name__ == '__main__':
    main()
