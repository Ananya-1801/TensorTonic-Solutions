import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    x = np.asarray(X)
    mean = np.mean(x,axis=0)
    x_centred = x - mean
    cov_matrix = np.dot(x_centred.T,x_centred)/(x.shape[0]-1)
    return cov_matrix