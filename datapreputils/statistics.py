import math
from statistics import median

def mode(data):
    frequency = {}
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes

def harmonic_mean(data):
    if len(data) == 0:
        return 0
    reciprocal_sum = sum(1 / x for x in data if x != 0)
    if reciprocal_sum == 0:
        return 0
    return len(data) / reciprocal_sum

def geometric_mean(data):
    if len(data) == 0:
        return 0
    product = math.prod(data)
    return product ** (1 / len(data))

def median_function(data):
    return median(data)
    