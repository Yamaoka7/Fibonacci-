def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
num_terms = 10
fib_sequence = fibonacci_sequence(num_terms)
print("Fibonacci sequence:", fib_sequence)
