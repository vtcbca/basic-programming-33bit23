2.def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

# Example usage
print(is_prime_recursive(11))  # Output: True
print(is_prime_recursive(15))  # Output: False
