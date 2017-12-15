"""
Day 10: Knot Hash
"""


class KnotHash:
    """
    Class using knot hash
    """

    def reverse(self, numbers, pos, length):
        """
        Method reversing specified elements in list
        :param numbers: list of numbers where substring will be reversed
        :param pos: starting element of array to reverse
        :param length: length of substring to reverse
        """
        curr_len = length - 1

        while curr_len > 0:
            ind1 = pos
            ind2 = (pos + curr_len) % len(numbers)
            numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]
            curr_len -= 2
            pos = (pos + 1) % len(numbers)

    def sparse_hash(self, nums):
        """
        "Perform xor operation necessary in Knoth algorithm
        """
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return format(ans, '02x')

    def hash_data(self, data):
        """
        Compute Knoth hash from data in input
        """
        numbers = [x for x in range(0, 256)]

        lengths = [ord(d) for d in data]
        lengths.extend([17, 31, 73, 47, 23])
        current_pos = 0
        skip_size = 0

        for _ in range(64):
            for length in lengths:
                self.reverse(numbers, current_pos, length)
                current_pos = (current_pos + length + skip_size) % len(numbers)
                skip_size += 1

        ans = ''
        for i in range(0, len(numbers), 16):
            ans += str(self.sparse_hash(numbers[i:i + 16]))
        return ans


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').read()
    knot_hash = KnotHash()
    ans = knot_hash.hash_data(data)
    print(ans)


if __name__ == '__main__':
    main()
