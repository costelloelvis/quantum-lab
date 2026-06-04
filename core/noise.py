import numpy as np

def depolarizing(rho, p=0.02):
    dim = rho.shape[0]
    I = np.eye(dim)

    return (1 - p) * rho + p * (I / dim)