from random import random


def random_event(p):
    def event():
        return 1 if random() <= p else 0

    return event


def complex_random_event(*p):
    events = [random_event(_p) for _p in p]

    def event():
        return 1 if all(e() == 1 for e in events) else 0

    return event


def complex_random_event_with_depending(pa, pb, pb_a, t=0):
    pb_na = (pb - pb_a * pa) / (1 - pa)
    events = [
        complex_random_event(pa, pb_a),
        complex_random_event(1 - pa, pb_na),
        complex_random_event(pa, 1 - pb_a),
        complex_random_event(1 - pa, 1 - pb_na)
    ]

    def event():
        return events[t]()

    return event


def random_event_group(k, *p):
    def event():
        return 1 if sum(p[:k - 1]) <= random() <= sum(p[:k]) else 0

    return event
