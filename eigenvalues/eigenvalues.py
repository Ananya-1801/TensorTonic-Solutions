import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    matrix = np.asarray(matrix,dtype=float)
    eigval = np.linalg.eigvals(matrix)
    return np.sort(eigval.real)
    