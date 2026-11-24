import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    x1 = np.asarray(x)
    p1 = np.asarray(p)
    return float(np.dot(x1,p1))