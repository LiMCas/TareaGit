import numpy as np

def min_max(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val) for x in data]

def z_score(data):
    mean = np.mean(data)
    std = np.std(data)
    return [round(float((x - mean) / std), 3) for x in data]

def mean_normalization(data):
    mean = np.mean(data)
    min_val = min(data)
    max_val = max(data)
    
    return [round(float((x - mean)) / (max_val - min_val),3) for x in data]