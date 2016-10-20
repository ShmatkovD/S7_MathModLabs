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
    start_value = 7364

    gen = initializeMultiplicative(start_value, 12345767, 1234769187)
    values = []

    n = 1000
    for i in xrange(n):
        values.append(gen.next())

    from drawer import draw
    draw(values, 20)
