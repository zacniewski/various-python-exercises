def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def counter(start, step):
    curr = start
    while True:
        yield curr
        curr += step

if __name__ == "__main__":
    print("Fibonacci(10):", list(fibonacci(10)))
    c = counter(10, 2)
    print("Counter(10, 2) first 5:", [next(c) for _ in range(5)])
