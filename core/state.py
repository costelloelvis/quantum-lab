import numpy as np

class QuantumState:
    def __init__(self, n_qubits=1):
        self.n = n_qubits
        dim = 2 ** n_qubits

        # |0...0><0...0|
        psi = np.zeros(dim, dtype=complex)
        psi[0] = 1

        self.rho = np.outer(psi, np.conjugate(psi))

    def apply(self, U):
        self.rho = U @ self.rho @ U.conj().T

    def get_probabilities(self):
        return np.real(np.diag(self.rho))