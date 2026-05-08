# Exercise 1: Argument Logger
# Create a decorator `debug` that prints the function name and the arguments it received.

def debug(func):
    # Your code here
    pass

@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Exercise 2: Timing Decorator (Bonus)
# Create a decorator `time_it` that measures the execution time of a function.
import time

def time_it(func):
    # Your code here
    pass

@time_it
def slow_function():
    time.sleep(1)
    return "Done"

if __name__ == "__main__":
    print(greet("Alice", greeting="Hi"))
    print(slow_function())
