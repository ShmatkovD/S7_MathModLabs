from matplotlib import pyplot


def initializeMiddleSquare(number):
    while True:
        number = number ** 2
        number = (number / 100) % 10000
        # yield number  # For check
        yield (number + 0.0) / 10000


def initializeMultiplicative(number, k, m):
    while True:
        number = (number * k) % m
        # yield number  # For check
        yield (number + 0.0) / m


if __name__ == '__main__':
    intervals = 10
    delta = 1.0 / intervals

    start_value = 7364

    gen = initializeMultiplicative(start_value, 12345767, 1234769187)
    values = []

    n = 1000
    for i in xrange(n):
        values.append(gen.next())

    diapasons = [
        (i * delta, (i + 1) * delta)
        for i in xrange(intervals)
    ]

    counts = [0 for _ in xrange(intervals)]

    for item in values:
        for i, diap in enumerate(diapasons):
            start, finish = diap
            if start <= item < finish:
                counts[i] += 1

    diapasons = [i for i, j in diapasons]
    counts = [(i + 0.0) / n for i in counts]

    pyplot.bar(diapasons, counts, width=delta * 0.8)
    pyplot.show()

    # Shift check
    s = 3

    pairs = []
    count = n - s
    for i in xrange(count):
        pairs.append(
            values[i] * values[i + s]
        )

    r = 12 * (1.0 / count) * sum(pairs) - 3

    print r




