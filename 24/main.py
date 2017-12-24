"""
Day 24: Electromagnetic Moat
"""


class Component:
    """
    Represents component with pines of the bridge
    """
    def __init__(self, pinstr):
        self.pin1, self.pin2 = list(map(int, pinstr.split('/')))

    def haspin(self, pinnum):
        """
        Check if component has got pin specified as argument
        """
        return pinnum in [self.pin1, self.pin2]

    def getsecondpin(self, first):
        """
        Component has 2 pins. Get pin different than first pin (given as an argument)
        """
        if first != self.pin1 and first != self.pin2:
            raise Exception('First pin does not exist in component')
        if first != self.pin1:
            return self.pin1
        return self.pin2

    def getweight(self):
        """
        Get weight of the component
        """
        return self.pin1 + self.pin2


class Bridge:
    """
    Class of single bridge
    """
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

class BridgeFinder:
    """
    Class used to find most optimal bridges
    """
    def __init__(self):
        self.components = []

    def add(self, component):
        """
        Add component to be considered while finding bridges
        """
        self.components.append(component)

    def getstrongestbridge(self):
        """
        Get bridge with the biggest weight
        """
        maxw = self._findbridge(0, self.components)
        return maxw

    def _findbridge(self, actpin, availablecomps):
        potentialcomps = [c for c in availablecomps if c.haspin(actpin)]
        bridgesums = []

        for comp in potentialcomps:
            availablecomps.remove(comp)
            bridgesum = self._findbridge(comp.getsecondpin(
                actpin), availablecomps) + comp.getweight()
            bridgesums.append(bridgesum)
            availablecomps.append(comp)
        if not bridgesums:
            return 0
        return max(bridgesums)

    def getlongestbridge(self):
        """
        Get bridge with the longest bridge
        """
        maxw = self._findlongestbridge(0, self.components)
        return maxw

    def _findlongestbridge(self, actpin, availablecomps):
        potentialcomps = [c for c in availablecomps if c.haspin(actpin)]
        bridgesums = []

        for comp in potentialcomps:
            availablecomps.remove(comp)
            bridge = self._findlongestbridge(comp.getsecondpin(actpin), availablecomps)
            bridge.weight += comp.getweight()
            bridge.length += 1
            bridgesums.append(bridge)
            availablecomps.append(comp)
        if not bridgesums:
            return Bridge(0, 0)
        bridgesums.sort(key=lambda x: x.weight, reverse=True)
        bridgesums.sort(key=lambda x: x.length, reverse=True)
        return bridgesums[0]


def main():
    """
    Main function
    """
    bridgefinder = BridgeFinder()
    data = open('input.txt', 'r').readlines()
    for pinpair in data:
        bridgefinder.add(Component(pinpair))
    print('Strongest: ', bridgefinder.getstrongestbridge())
    print('Longest: ', bridgefinder.getlongestbridge().weight)


if __name__ == '__main__':
    main()
