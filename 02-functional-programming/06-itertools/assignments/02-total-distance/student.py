from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def total_distance(path, distance):
    return sum(distance(a, b) for a, b in pairwise(path))