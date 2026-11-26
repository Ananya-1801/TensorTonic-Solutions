import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    x = np.asarray(matrix,dtype=float)
    if norm_type == "l1":
        norms = np.sum(np.abs(x),axis=axis,keepdims=True)
    elif norm_type=="l2":
        norms = np.sqrt(np.sum(x**2,axis=axis,keepdims=True))
    elif norm_type=="max":
        norms = np.max(np.abs(x),axis=axis,keepdims=True)
    else:
        raise ValueError("Invalid normalization type")
    norms = np.where(norms==0,1.0,norms)
    return x/norms