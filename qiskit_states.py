import numpy as np

def create_qiskit_basis_state(qubit_count: int,
                              data: tuple):
    # replace numpy encoding with actual qiskit state creation
    if qubit_count == 1:
        qiskit_basis_state = np.array(data)
    else:
        qiskit_basis_state = None
    return qiskit_basis_state