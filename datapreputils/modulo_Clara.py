import math

def harmonic_mean(data):
    if len(data) == 0:
        return 0
    reciprocal_sum = sum(1 / x for x in data if x != 0)
    if reciprocal_sum == 0:
        return 0
    return len(data) / reciprocal_sum
