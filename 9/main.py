"""
Day 9: Stream Processing
"""

def main():
    data = open('input.txt', 'r').read()
    score = 0
    value = 0
    garbage = False
    exclamation = False
    garbage_count = 0

    for char in data:
        if exclamation:
            exclamation = False
            continue
        elif char == '!':
            exclamation = True
            continue
        elif char == '>':
            garbage = False
        elif garbage:
            garbage_count += 1
            continue
        elif char == '<':
            garbage = True
        elif char == '{':
            value += 1
        elif char == '}':
            score += value
            value = max(value - 1, 0)
        

    print('score:', score)
    print('garbage count:', garbage_count)


if __name__ == '__main__':
    main()
