from functools import wraps
from time import perf_counter


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{function.__name__} completed in {elapsed:.6f}s")
        return result
    return wrapper


@measure_time
def add_numbers(left: int, right: int) -> int:
    return left + right

print(add_numbers(3, 4))
