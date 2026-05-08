# Exercise 1: Fibonacci Generator
# Write a generator function `fibonacci(n)` that yields the first `n` Fibonacci numbers.
# Recall: 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    # Your code here
    pass

# Test your code
if __name__ == "__main__":
    print(list(fibonacci(10)))
    # Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Exercise 2: Infinite Counter with Step
# Write a generator `counter(start, step)` that yields numbers starting from `start` 
# and increments by `step` indefinitely. Use it to print the first 5 numbers.

def counter(start, step):
    # Your code here
    pass

if __name__ == "__main__":
    c = counter(10, 2)
    for _ in range(5):
        print(next(c))
    # Expected: 10, 12, 14, 16, 18
