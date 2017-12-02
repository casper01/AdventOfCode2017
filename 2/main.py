"""
Day 2: Corruption Checksum
"""

def main():
    data = open('input.txt', 'r')
    ans = 0

    for row in data.readlines():
        values = row.split()
        values = list(map(int, values))
        max_val = max(values)
        min_val = min(values)

        # evenly divisible values
        checksum = 0
        for i in range(0, len(values)):
            for j in range(i, len(values)):
                if i == j:
                    continue
                bigger = max(values[i], values[j])
                smaller = min(values[i], values[j])

                if bigger / smaller == int(bigger / smaller):
                    checksum = int(bigger / smaller)
                    break
            if checksum != 0:
                break

        # checksum = max_val - min_val
        ans += checksum

    print(ans)


if __name__ == '__main__':
    main()
