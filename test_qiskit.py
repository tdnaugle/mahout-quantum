from numpy_states import create_np_basis_state
from qiskit_states import create_qiskit_basis_state
import numpy as np

#using pytest, attempt to initialize states in qiskit
def test_single_qubit_basis():
    # example test between np representation of basis state and qiskit representation of basis state
    assert create_np_basis_state(1, (1,0)).size == create_qiskit_basis_state(1, (1,0)).size