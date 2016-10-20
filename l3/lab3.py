from __future__ import unicode_literals, absolute_import

import math
from random import random, seed

from drawer import draw

seed(57123)


def exponential(lamda=2, rand=random, length=1000):
    return [
        - math.log(rand()) / lamda
        for _ in xrange(length)
    ]


def normal(m=0, sigma=1, n=12, length=1000):
    return [
        m + sigma * math.sqrt(12/n) * (
                sum([random() for _ in xrange(n)]) - n/2
        )
        for _ in xrange(length)
    ]


def triangle(a=0, b=2, rand=random, length=100000):
    return [
        a + (b - a) * max(rand(), rand()) for _ in xrange(length)
    ]


def simpson(a=0, b=2, rand1=random, rand2=random, length=1000):
    return [
        rand1() + rand2()
        for _ in xrange(length)
    ]

if __name__ == '__main__':
    sample = exponential()

    draw(sample, 20)
