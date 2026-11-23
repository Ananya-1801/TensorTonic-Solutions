from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    count = Counter(x)
    max_freq = max(count.values())

    mode = min(value for value,freq in count.items()
               if freq==max_freq)
    return { "mean":float(np.mean(x)),
           "median":float(np.median(x)),
           "mode":float(mode)}