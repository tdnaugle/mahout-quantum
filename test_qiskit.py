from numpy_states import create_np_computational_basis_state
from qiskit_states import create_qiskit_basis_state

# Using pytest, attempt to initialize states in qiskit
def test_basis_state(test_qubit_count=2,
                    test_ket_str="01"):
    # np representation
    np_basis_state = create_np_computational_basis_state(test_qubit_count, test_ket_str)

    # qiskit representation
    qiskit_basis_state = create_qiskit_basis_state(test_qubit_count, test_ket_str)
    qiskit_basis_state_data = qiskit_basis_state.data

    # Compare size
    assert np_basis_state.size == qiskit_basis_state_data.size
    # Compare entry types
    assert np_basis_state.dtype == qiskit_basis_state_data.dtype
