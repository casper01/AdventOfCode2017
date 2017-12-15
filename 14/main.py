"""
Day 14: Disk Defragmentation
"""

from enum import Enum
from knothash import KnotHash

BIN_SIZE = 4
HEX_BASE = 16


def hexhash2binhash(hexhash):
    """
    Converts every char of hex hash to bin hash
    """
    binhash = []
    for char in hexhash:
        binhash.append(bin(int(char, HEX_BASE))[2:].zfill(BIN_SIZE))
    return ''.join(binhash)


class Memory:
    """
    Represents memory of the task
    """
    MARKED_REGION = 'x'
    UNMARKED_REGION = '#'
    EMPTY_REGION = '.'

    @staticmethod
    def bin2memory(bin_str):
        """
        Converts binary string to valid memory string
        """
        ans = map(lambda x: Memory.UNMARKED_REGION if x ==
                  '1' else Memory.EMPTY_REGION, bin_str)
        return ''.join(list(ans))

    def __init__(self, data):
        self.memory = []
        self.construct_matrix(data)

    def construct_matrix(self, data):
        """
        Constructs square matrix according to task conditions
        """
        self.memory = []
        knot_hash = KnotHash()
        for i in range(128):
            row = str(data) + '-' + str(i)
            hashed_row = knot_hash.hash_data(row)
            hashed_row = hexhash2binhash(hashed_row)
            hashed_row = Memory.bin2memory(hashed_row)
            self.memory.append(hashed_row)

    def get_neighbours(self, i, j):
        """
        Get indices of neighbouring memory elements of specified element
        :param i: first index of specified element
        :param j: second index of specified element
        :return: list of indices pairs
        """
        neighbours = []
        if i - 1 >= 0:
            neighbours.append((i - 1, j))
        if j - 1 >= 0:
            neighbours.append((i, j - 1))
        if i + 1 < len(self.memory):
            neighbours.append((i + 1, j))
        if j + 1 < len(self.memory[i]):
            neighbours.append((i, j + 1))
        return neighbours

    def flood_fill(self, i, j, source_val, dest_val):
        """
        Performs flood fill operation.
        Swaps all source_val elements to dest_val elements that are neighbours of (i, j) element
        :param i: first index of starting element
        :param j: second index of starting element
        :param source_val: char value of element to swap
        :param dest_val: char value of element on which source_val will be swapped
        """
        to_analyze = [(i, j)]
        analyzed = []

        while to_analyze:
            i, j = to_analyze.pop()
            if self.memory[i][j] != source_val:
                continue
            self.memory[i] = self.memory[i][:j] + \
                str(dest_val) + self.memory[i][j + 1:]
            analyzed.append((i, j))
            neighbours = self.get_neighbours(i, j)
            to_analyze.extend(
                [n for n in neighbours if self.memory[n[0]][n[1]] == source_val])
        return analyzed

    def compute_regions(self):
        """
        Compute number of consistent regions in memory
        :return: Number of consistent regions
        """
        regions_count = 0

        for i in range(len(self.memory)):
            for j in range(len(self.memory[i])):
                if self.memory[i][j] != Memory.UNMARKED_REGION:
                    continue
                regions_count += 1
                self.flood_fill(i, j, Memory.UNMARKED_REGION,
                                Memory.MARKED_REGION)
        return regions_count

    def hashes_count(self):
        """
        Compute number of not empty regions in memory
        :return: Number of not empty regions
        """
        return sum([1 if c == Memory.UNMARKED_REGION
                    else 0 for row in self.memory for c in row])


def main():
    """
    Main function
    """
    # data = open('input.txt', 'r').read()
    data = 'flqrgnkx'
    memory = Memory(data)

    hashes_count = memory.hashes_count()
    print('Hashes count:', hashes_count)

    regions_count = memory.compute_regions()
    print('Consistent regions count:', regions_count)


if __name__ == '__main__':
    main()
