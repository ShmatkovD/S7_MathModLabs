from __future__ import unicode_literals, absolute_import

from random import random, seed
from matplotlib import pyplot

seed(45768)


def spread_values(probabilities, values):
    x_axis = [i for i in xrange(len(probabilities))]

    counts = []
    for i, prob in enumerate(probabilities):
        count = 0
        l_bound = sum(probabilities[:i])
        r_bound = l_bound + prob

        for value in values:
            count += 1 if l_bound <= value < r_bound else 0

        counts.append(count)

    return x_axis, counts


if __name__ == '__main__':
    n = 100000
    sample = [random() for _ in xrange(n)]

    probabilities = [0.2, 0.1, 0.25, 0.05, 0.4]
    assert sum(probabilities) <= 1, " >1!!!!"

    if sum(probabilities) < 1:
        probabilities.append(1 - sum(probabilities))

    values, counts = spread_values(probabilities, sample)

    pyplot.bar(values, counts, width=1)
    pyplot.show()
