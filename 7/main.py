"""
Day 7: Recursive Circus
"""


class DataElement:
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.subs = []

    @staticmethod
    def create_from_string(line):
        info = line.split()
        element = DataElement(info[0], info[1][1:-1])

        for i in range(3, len(info)):
            sub = info[i] if info[i][-1] != ',' else info[i][0:-1]
            element.add_sub(sub)
        return element

    def add_sub(self, sub):
        self.subs.append(sub)

    def subtree_weight(self):
        weight = self.weight
        weight += sum([s.subtree_weight() for s in self.subs])
        return weight

    def is_balanced(self):
        distinct_weights = len(
            list(set([el.subtree_weight() for el in self.subs])))
        return distinct_weights <= 1

    def get_different_sub(self):
        if len(self.subs) == 2 and not self.is_balanced():
            raise Exception('Tree does not meet task conditions')
        # assumption: only one sub is different
        subs = [(sub, sub.subtree_weight()) for sub in self.subs]
        subs = sorted(subs, key=lambda sub: sub[1])
        return subs[0][0] if subs[0][1] != subs[1][1] else subs[-1][0]

    def get_lowest_unbalanced_node(self):
        if self.is_balanced():
            raise Exception('Tree is balanced')
        for sub in self.subs:
            if not sub.is_balanced():
                return sub.get_lowest_unbalanced_node()
        return self


def create_data_list(data):
    data_elements = []

    for line in data:
        data_elements.append(DataElement.create_from_string(line))

    # repair tree - set objects instead of strings
    data_elements.sort(key=lambda x: len(x.subs))
    for element in data_elements:
        element.subs = [el for el in data_elements if el.name in element.subs]

    return data_elements


def get_elements_list_root(elements):
    subs = [s for e in elements for s in e.subs]
    subs = list(set(subs))
    return next(el for el in elements if el not in subs)


def main():
    data = open('input.txt', 'r').readlines()
    data_elements = create_data_list(data)
    root = get_elements_list_root(data_elements)
    print('Part 1 ans: ', root.name)

    unbalanced_node = root.get_lowest_unbalanced_node()
    different_sub = unbalanced_node.get_different_sub()
    subtree_weights = [el.subtree_weight() for el in unbalanced_node.subs]
    max_weight = max(subtree_weights)
    min_weight = min(subtree_weights)
    sub_weight = different_sub.subtree_weight()
    diff = max_weight - min_weight
    diff *= -1 if sub_weight == max_weight else 1
    ans = different_sub.weight + diff
    print('Part 2 ans: ', ans)


if __name__ == '__main__':
    main()
