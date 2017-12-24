"""
Day 20: Particle Swarm
"""

import sys


class Particle:
    """
    Represents moving particle
    """
    @staticmethod
    def _getvector(string):
        start = string.index('<')
        end = string.index('>')
        string = string[start + 1:end]
        return list(map(int, string.split(',')))

    @staticmethod
    def createfromstring(pid, string):
        """
        Create particle object from valid string
        :param string: string valid according to task assumptions
        :return: Particle object
        """
        _, pos, vel, acc = string.split('=')
        pos = Particle._getvector(pos)
        vel = Particle._getvector(vel)
        acc = Particle._getvector(acc)
        return Particle(pid, pos, vel, acc)

    @staticmethod
    def detectpointsofcolision(particles):
        """
        Get points in which there are located the same particles
        :param particles: list of Particle objects
        :return: list of strings - vectors of location of collision
        """
        uniquepts = {}
        for part in particles:
            if str(part.pos) in uniquepts:
                uniquepts[str(part.pos)] = False
            else:
                uniquepts[str(part.pos)] = True
        return [pt for pt in uniquepts if not uniquepts[pt]]

    def __init__(self, pid, p, v, a):
        self.pid = pid
        self.pos = p
        self.vel = v
        self.acc = a

    def accnorm(self):
        """
        Get norm value of acceleration
        """
        return sum(map(abs, self.acc))

    def posnorm(self, time=0):
        """
        Get norm value of position
        """
        pos = self.getpos(time)
        return sum(map(abs, pos))

    def vnorm(self):
        """
        Get norm value of velocity
        """
        return sum(map(abs, self.vel))

    def getpos(self, time):
        """
        Get position in specified time moment
        :param time: Iteration number
        :return: Position vector
        """
        vel = self.vel
        acc = self.acc
        pos = self.pos
        for _ in range(time):
            vel = list(map(sum, zip(vel, acc)))
            pos = list(map(sum, zip(pos, vel)))
        return pos

    def move(self):
        """
        Make one move of the particle
        """
        self.vel = list(map(sum, zip(self.vel, self.acc)))
        self.pos = list(map(sum, zip(self.pos, self.vel)))

    def getvchangemoment(self):
        """
        Get number of moments needed to make velocity vector have the same sign
        in all dimensions as acceleration vector
        """
        moment = 0
        vel = self.vel
        acc = self.acc
        pos = self.pos
        while not all(tup[0] * tup[1] >= 0 for tup in zip(vel, acc)):
            vel = list(map(sum, zip(vel, acc)))
            pos = list(map(sum, zip(pos, vel)))
            moment += 1
        return moment


def main():
    """
    Main function
    """
    data = open('input.txt', 'r').readlines()
    particles = []

    # find minimal acceleration
    minacc = sys.maxsize
    for actpid, partstring in enumerate(data):
        particle = Particle.createfromstring(actpid, partstring)
        particles.append(particle)
        if particle.accnorm() < minacc:
            minacc = particle.accnorm()

    slowestparticles = [p for p in particles if p.accnorm() == minacc]
    smallestv = min(p.vnorm() for p in slowestparticles)
    closestp = next(p for p in slowestparticles if p.vnorm() == smallestv)
    print('closest particle:', closestp.pid)

    iteration = 0
    maxvchangemoment = max(p.getvchangemoment() for p in particles)

    while True:
        for part in particles:
            part.move()
        duplicates = Particle.detectpointsofcolision(particles)
        if duplicates:
            particles = [part for part in particles if str(
                part.pos) not in duplicates]
        elif iteration > maxvchangemoment:
            string1 = sorted(particles, key=lambda x: x.posnorm())
            string2 = sorted(particles, key=lambda x: x.vnorm())
            string1 = [p.vnorm() for p in string1]
            string2 = [p.vnorm() for p in string2]
            if string1 == string2:
                break
        iteration += 1
    print('particles left: ', len(particles))


if __name__ == '__main__':
    main()
