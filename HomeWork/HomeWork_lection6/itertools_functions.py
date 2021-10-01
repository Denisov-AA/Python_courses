import itertools


def sum_of_arrays(*args):
    return list(itertools.chain(*args))


def length_control(*args: str, length=5):
    return list(itertools.filterfalse(lambda x: len(x) < length, [*args]))


def combinations(string, length):
    return list(itertools.combinations(string, length))
