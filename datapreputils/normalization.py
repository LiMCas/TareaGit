import numpy as np

def min_max(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val) for x in data]

def z_score(data):
    mean = np.mean(data)
    std = np.std(data)
    return [round(float((x - mean) / std), 3) for x in data]