# Calculate the nth Fibonacci Number Efficiently
# Based on the iterative dynamic programming approach outlined in Experiment 4

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# Main Program
if __name__ == "__main__":
    n_values = [0, 1, 5, 10, 50, 100]
    print("Efficient Iterative Fibonacci Calculation:")
    for n in n_values:
        print(f"F({n}) = {fibonacci_iterative(n)}")