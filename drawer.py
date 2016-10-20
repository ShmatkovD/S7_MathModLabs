from matplotlib import pyplot


def draw(sequense, diap_count=10):

    min_value = min(*sequense)
    max_value = max(*sequense)

    step = (max_value - min_value) / diap_count

    values = []
    counts = []

    current_value = min_value
    for _ in xrange(diap_count):
        values.append(current_value + step / 2)
        count = 0

        for item in sequense:
            count += 1 if current_value <= item < current_value + step else 0

        counts.append(count)
        current_value += step

    pyplot.bar(values, counts, width=step)
    pyplot.show()
