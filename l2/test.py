import math
import matplotlib.pyplot as plt
import operator

from task import random_event, complex_random_event, complex_random_event_with_depending, random_event_group


def visualize(func, n=100000, bins=10):
    x = [func() for _ in xrange(n)]

    plt.hist(x, bins)
    plt.show()


N = 100000
EPS = 1e-2


def _assert(expected, actual):
    if math.fabs(expected - actual) < EPS:
        print 'ok'
    else:
        print 'failed (actual: {}, expected: {})'.format(actual, expected)


def test_event(event, p):
    s = sum(event() for _ in xrange(N))
    actual_p = float(s) / N

    _assert(p, actual_p)


def test_random_event():
    print 'test_random_event:'

    p = 0.3

    event = random_event(p)
    test_event(event, p)
    visualize(event, n=N, bins=20)


def test_complex_random_event():
    print 'test_complex_random_event:'

    p = [0.8, 0.2]

    event = complex_random_event(*p)
    expected = reduce(operator.mul, p)
    test_event(event, expected)
    visualize(event, n=N, bins=20)


def test_complex_random_event_with_depending():
    print 'test_complex_random_event_with_depending:'

    pa = 0.3
    pb = 0.5
    pb_a = 0.2
    events = [complex_random_event_with_depending(pa, pb, pb_a, t) for t in xrange(4)]

    total = 0
    for i, event in enumerate(events):
        x = sum(event() for _ in xrange(N))
        total += x
        plt.bar(i - 0.1, x, width=0.2)
    _assert(1.0, float(total) / N)
    plt.xticks(range(4), ('AB', 'A(-B)', '(-A)B', '(-A)(-B)'))
    plt.show()


def test_random_event_group():
    print 'test_random_event_group:'

    p = [0.49, 0.49, 0.02]
    k = len(p)
    events = [random_event_group(_k + 1, *p) for _k in xrange(k)]

    total = 0
    for i, event in enumerate(events):
        x = sum(event() for _ in xrange(N))
        total += x
        plt.bar(i - 0.1, x, width=0.2)
    _assert(1.0, float(total) / N)
    plt.xticks(range(k), map(str, xrange(1, k + 1)))
    plt.show()


def test():
    test_random_event()
    test_complex_random_event()
    test_complex_random_event_with_depending()
    test_random_event_group()


if __name__ == '__main__':
    test()
