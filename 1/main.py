"""
Day 1: Inverse Captcha
"""

def main():
    data = open('input.txt', 'r').read()
    # data = '123123'

    summ = 0
    step = int(len(data) / 2)
    for i in range(0, len(data)):
        j = (i + step) % len(data)
        if data[i] == data[j]:
            summ += int(data[i])
    print(summ)


if __name__ == '__main__':
    main()
