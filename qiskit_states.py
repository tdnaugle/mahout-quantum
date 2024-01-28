import numpy as np
from qiskit.quantum_info import Statevector
from typing import List

def create_qiskit_basis_state(qubit_count: int,
                              ket_str: str):
    qiskit_basis_state = Statevector.from_label(ket_str)

    return qiskit_basis_state