from numpy_states import create_np_computational_basis_state, BinaryString
from qiskit_states import create_qiskit_basis_state
import numpy as np


# Using pytest, attempt to initialize states in qiskit
def test_computational_basis_state(ket_str: BinaryString = "01"):
    # np representation
    np_basis_state = create_np_computational_basis_state(ket_str)

    # qiskit representation
    qiskit_basis_state = create_qiskit_basis_state(ket_str)
    qiskit_basis_state_data = qiskit_basis_state.data

    # Compare size
    assert np_basis_state.size == qiskit_basis_state_data.size
    # Compare entry data types
    assert np_basis_state.dtype == qiskit_basis_state_data.dtype
    # Compare entry values
    assert np.array_equal(np_basis_state, qiskit_basis_state_data)


# TODO: complete this function
def test_all_computational_basis_states(qubit_count: int = 2):
    None