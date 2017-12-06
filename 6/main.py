import math
import copy

"""
Day 6: Memory Reallocation
"""


def reallocateNumber(data, index):
    number = data[index]
    num_per_cell = math.ceil(number / len(data))

    data[index] = 0
    act_ind = index
    while number > 0:
        act_ind = (act_ind + 1) % len(data)
        if number - num_per_cell >= 0:
            data[act_ind] += num_per_cell
            number -= num_per_cell
        else:
            data[act_ind] += number
            number = 0


def listsAreEqual(list1, list2):
    if len(list1) != len(list2):
        return False
    return all(list1[i] == list2[i] for i in range(0, len(list1)))


def wasMetPreviously(list1, previousLists):
    try:
        ind = previousLists.index(list1)
        return True, ind
    except ValueError:
        return False, None


def main():
    data = open('input.txt', 'r').read().split()
    # data = '0 2 7 0'.split()
    data = list(map(int, data))
    previous = []

    times = 0
    areEqual = False

    while not areEqual:
        previous.append(copy.deepcopy(data))
        max_ind = data.index(max(data))
        reallocateNumber(data, max_ind)
        times += 1
        areEqual, equalInd = wasMetPreviously(data, previous)

    print("times: ", times)
    print("cycles: ", len(previous) - equalInd)


if __name__ == '__main__':
    main()
