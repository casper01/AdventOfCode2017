"""
Day 10: Knot Hash
"""

def reverse(numbers, pos, length):
    curr_len = length - 1

    while curr_len > 0:
        ind1 = pos
        ind2 = (pos + curr_len) % len(numbers)
        numbers[ind1], numbers[ind2] = numbers[ind2], numbers[ind1]
        curr_len -= 2
        pos = (pos + 1) % len(numbers)

def sparse_hash(nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = ans ^ nums[i]
    return format(ans, '02x')



def main():
    data = open('input.txt', 'r').read()
    numbers = [x for x in range(0,256)]

    lengths =  [ord(d) for d in data]
    lengths.extend([17, 31, 73, 47, 23])
    print(lengths)
    current_pos = 0
    skip_size  =0

    for _ in range(64):
        for length in lengths:
            reverse(numbers, current_pos, length)
            current_pos = (current_pos + length + skip_size) % len(numbers)
            skip_size += 1

    ans = ''
    for i in range(0, len(numbers), 16):
        ans += str(sparse_hash(numbers[i:i+16]))

    print(ans)


    # ans = numbers[0] * numbers[1]
    # print('ans = ', ans)
    

    

if __name__ == '__main__':
    main()
