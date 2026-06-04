import numpy as np

H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

X = np.array([[0, 1],
              [1, 0]])

I = np.eye(2)

def kron(*ops):
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result

# 2-qubit gates
H0 = kron(H, I)
CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])