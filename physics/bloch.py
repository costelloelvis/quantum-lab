import numpy as np

def bloch_vector(rho):
    x = np.real(rho[0,1] + rho[1,0])
    y = np.imag(rho[1,0] - rho[0,1])
    z = np.real(rho[0,0] - rho[1,1])

    return x, y, z