"""
Day 4: High-Entropy Passphrases
"""


def isValidPassphrase(passphrase):
    words = passphrase.split()
    unique = {}
    for word in words:
        if word in unique:
            return False
        unique[word] = True
    return True


def isSuperValidPassphrase(passphrase):
    words = passphrase.split()
    unique = {}
    for word in words:
        word = ''.join(sorted(word))
        if word in unique:
            return False
        unique[word] = True
    return True


def main():
    data = open('input.txt', 'r').readlines()

    count = 0
    for passphrase in data:
        if isValidPassphrase(passphrase):
            count += 1
    print(count)

    count = 0
    for passphrase in data:
        if isSuperValidPassphrase(passphrase):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
