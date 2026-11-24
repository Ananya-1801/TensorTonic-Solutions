import numpy as np

def sample_var_std(x: list) -> dict:
    x = np.asarray(x,dtype=float)
    c = x - np.mean(x)
    var = float(np.sum(c**2)/(x.size-1))
    sd = float(np.sqrt(var))
    return {'variance':var,'standard_deviation':sd}