from clockedeco import clock
from functools import cache
import time


@cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

@clock
@cache
def test_cache(*args):
    time.sleep(args[0])
    return args


if __name__ == "__main__":
    fibonacci(31)
    for i in (1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5):
        print(test_cache(i))

    print(test_cache(1))
