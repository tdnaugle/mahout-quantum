import functools
import sys

def trace_calls_with_filter(filter_str):
    """
    Example usage of printing the qiskit-only calls from a qiskit operation:

    @trace_calls_with_filter("qiskit")
    def trace_state_vector():
        qiskit_basis_state = Statevector.from_label("01")


    if __name__ == "__main__":
        trace_state_vector()
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def trace_calls(frame, event, arg):
                if event != 'call':
                    return
                code = frame.f_code
                filename = code.co_filename
                if filter_str in filename:
                    print(f"Call to {code.co_name} in {filename}: {frame.f_lineno}")

            sys.settrace(trace_calls)
            result = func(*args, **kwargs)
            sys.settrace(None)
            return result

        return wrapper

    return decorator


