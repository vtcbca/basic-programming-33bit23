
3.def fibonacci_recursive(terms, a=0, b=1, sequence=None):
    if sequence is None:
        sequence = []
    if terms == 0:
        return sequence
    sequence.append(a)
    return fibonacci_recursive(terms - 1, b, a + b, sequence)

# Example usage
print(fibonacci_recursive(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]