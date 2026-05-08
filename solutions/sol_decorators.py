import functools
import time

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"DEBUG: Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"TIME: {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

@time_it
def slow_function():
    time.sleep(0.5)
    return "Done"

if __name__ == "__main__":
    print(greet("Alice", greeting="Hi"))
    print(slow_function())
