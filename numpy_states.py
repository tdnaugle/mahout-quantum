import numpy as np
from typing import List
from functools import reduce

# Initialize basis state as numpy array
def create_np_computational_basis_state(qubit_count: int,
                                        ket_str: str,
                                        np_dtype: str = "complex128") -> np.array:
    single_qubit_state_dict = {
                            "0": np.array([1, 0], dtype=np_dtype),
                            "1": np.array([0, 1], dtype=np_dtype)
                            }

    single_qubit_vectors = map(single_qubit_state_dict.get, ket_str)
    computational_basis_vector = reduce(lambda x, y: np.kron(x, y), single_qubit_vectors)

    return computational_basis_vector
