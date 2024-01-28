import numpy as np 

# initialize basis state as numpy array
def create_np_basis_state(qubit_count: int,
                          data: tuple) -> np.array:
    if qubit_count == 1:
        np_basis_state = np.array(data)
    else:
        np_basis_state = None

    return np_basis_state

# initialize bell state (as tuple of numpy array?)