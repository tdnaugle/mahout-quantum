import numpy as np
from qiskit.quantum_info import Statevector
from typing import List

def create_qiskit_basis_state(ket_str: str) -> Statevector:
    qiskit_basis_state = Statevector.from_label(ket_str)

    return qiskit_basis_state