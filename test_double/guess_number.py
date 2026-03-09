import random


def guess_int(start, stop):
    return random.randint(start, stop)


def guess_float(start, stop):
    return random.uniform(start, stop)
