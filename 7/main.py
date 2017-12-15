"""
Day 7: Recursive Circus
"""


class DataElement:
    """
    Represents tree node: a process
    """
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.subs = []

    @staticmethod
    def create_node_from_string(line):
        """
        Create DataElement from proper definition of node
        :param line: string definition of node
        :return: DataElement instance with subs as strings
        """
        info = line.split()
        element = DataElement(info[0], info[1][1:-1])

        for i in range(3, len(info)):
            sub = info[i] if info[i][-1] != ',' else info[i][0:-1]
            element.add_sub(sub)
        return element

    @staticmethod
    def create_tree(data):
        """
        Create tree of proper list of nodes definition described in task
        :param data: list of nodes definition
        :return: node of created tree
        """
        elements = DataElement.create_data_list(data)
        subs = [s for e in elements for s in e.subs]
        subs = list(set(subs))
        return next(el for el in elements if el not in subs)

    @staticmethod
    def create_data_list(data):
        """
        Creates list of nodes from proper data string.
        Every node is configured properly - has got valid pointers
        """
        data_elements = []

        for line in data:
            data_elements.append(DataElement.create_node_from_string(line))

        # repair tree - set objects instead of strings
        data_elements.sort(key=lambda x: len(x.subs))
        for element in data_elements:
            element.subs = [el for el in data_elements if el.name in element.subs]

        return data_elements

    def add_sub(self, sub):
        """
        Add subprocess
        :sub: DataElement instance, subprocess of current process
        """
        self.subs.append(sub)

    def subtree_weight(self):
        """
        Compute weight of tree with a root in current elements
        :return: Sum of own weight and weights of subrocesses
        """
        weight = self.weight
        weight += sum([s.subtree_weight() for s in self.subs])
        return weight

    def is_balanced(self):
        """
        Checks if all subprocesses have got the same subtree weigth
        :return: true if is balanced, otherwise false
        """
        distinct_weights = len(
            list(set([el.subtree_weight() for el in self.subs])))
        return distinct_weights <= 1

    def get_different_sub(self):
        """
        Method assumes that all but one subprocesses have got the same subtree weight.
        Finds the process which subtree weight differs
        :return: The differing node
        """
        if len(self.subs) == 2 and not self.is_balanced():
            raise Exception('Tree does not meet task conditions')
        # assumption: only one sub is different
        subs = [(sub, sub.subtree_weight()) for sub in self.subs]
        subs = sorted(subs, key=lambda sub: sub[1])
        return subs[0][0] if subs[0][1] != subs[1][1] else subs[-1][0]

    def get_lowest_unbalanced_node(self):
        """
        Method assumes that the subtree with root in current node is unbalanced and
        only one subnode causes this fact.
        It finds this subnode
        :return: Subnode causing that the tree is unbalanced
        """
        if self.is_balanced():
            raise Exception('Tree is balanced')
        for sub in self.subs:
            if not sub.is_balanced():
                return sub.get_lowest_unbalanced_node()
        return self




def main():
    """
    Main function
    """
    data = open('input.txt', 'r').readlines()
    root = DataElement.create_tree(data)
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
