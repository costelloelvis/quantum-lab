import numpy as np

def measure(rho):
    probs = np.real(np.diag(rho))
    probs = probs / np.sum(probs)

    outcome = np.random.choice(len(probs), p=probs)

    collapsed = np.zeros_like(rho)
    collapsed[outcome, outcome] = 1.0

    return outcome, collapsed