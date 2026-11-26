import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    x = np.asarray(X,dtype=float)
    N = x.shape[0]
    centred = x - np.mean(x,axis=0)
    cov = np.dot(centred.T,centred)/(N-1)
    std = np.sqrt(np.diag(cov))
    denom = np.outer(std,std)
    corr = np.full_like(cov,np.nan,dtype=float)
    np.divide(cov,denom,out=corr,where=denom!=0)
    return corr
    