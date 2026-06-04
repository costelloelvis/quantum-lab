# QuantumLab

QuantumLab is a Python-based educational quantum computing simulator designed to demonstrate the fundamentals of quantum mechanics, quantum information, and quantum computation through interactive simulations and visualizations.

The project provides tools for creating quantum states, applying quantum gates, modeling noise, visualizing Bloch sphere dynamics, and exploring quantum measurement processes.

---

## Features

### Quantum States

* Single and multi-qubit state representation
* State vector simulation
* Quantum state evolution

### Quantum Gates

* Hadamard Gate (H)
* Pauli-X Gate
* Controlled-NOT (CNOT)
* Custom gate support

### Quantum Noise

* Depolarizing noise channel
* Noise-aware simulations
* Quantum decoherence demonstrations

### Quantum Measurements

* State collapse simulation
* Measurement probabilities
* Observable outcomes

### Bloch Sphere Physics

* Bloch vector calculations
* Qubit state visualization
* Quantum state trajectory analysis

### Interactive Visualization

* Dashboard interface
* Real-time simulation updates
* Educational quantum experiments

---

## Project Structure

```text
QuantumLab/
│
├── core/
│   ├── __init__.py
│   ├── state.py
│   ├── gates.py
│   └── noise.py
│
├── physics/
│   ├── __init__.py
│   ├── bloch.py
│   └── measurement.py
│
├── viz/
│   ├── __init__.py
│   ├── dashboard.py
│   └── theme.py
│
├── run.py
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/costelloelvis/quantum-lab.git
cd QuantumLab
```

Create a virtual environment:

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install required packages:

```bash
pip install numpy matplotlib
```

Or using requirements:

```bash
pip install -r requirements.txt
```

---

## Running QuantumLab

Launch the application:

```bash
python run.py
```

---

## Example: Bell State Creation

```python
from core.state import QuantumState
from core.gates import H0, CNOT

q = QuantumState(2)

q.apply(H0)
q.apply(CNOT)

print(q.state)
```

This generates the Bell state:

```text
(|00⟩ + |11⟩)/√2
```

which is one of the simplest examples of quantum entanglement.

---

## Educational Topics Covered

* Qubits
* Superposition
* Entanglement
* Quantum Gates
* State Evolution
* Quantum Measurements
* Noise and Decoherence
* Bloch Sphere Representation

---

## Technologies Used

* Python 3
* NumPy
* Matplotlib

---

## Future Roadmap

* [ ] Quantum teleportation
* [ ] Grover's search algorithm
* [ ] Quantum Fourier Transform
* [ ] Multi-qubit visualization
* [ ] Quantum error correction
* [ ] Qiskit integration
* [ ] IBM Quantum hardware support
* [ ] Quantum machine learning experiments

---

## Author

**Elvis Wanjiru**

Physics • Quantum Computing • Scientific Programming

GitHub: https://github.com/costelloelvis

---

## License

MIT License

---

### QuantumLab Mission

> To provide an accessible and practical environment for learning quantum computing through simulation, visualization, and experimentation.
