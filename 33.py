solution


1.def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
print(factorial_recursive(5))  # Output: 120


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


3.def fibonacci_recursive(terms, a=0, b=1, sequence=None):
    if sequence is None:
        sequence = []
    if terms == 0:
        return sequence
    sequence.append(a)
    return fibonacci_recursive(terms - 1, b, a + b, sequence)

# Example usage
print(fibonacci_recursive(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


4.def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

# Example usage
print(reverse_string_recursive("hello"))  # Output: "olleh"


5.def is_palindrome_recursive(s, left=0):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    right = len(s) - 1 - left
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome_recursive(s, left + 1)

# Example usage
print(is_palindrome_recursive("A man a plan a canal Panama"))  # Output: True
print(is_palindrome_recursive("hello"))  # Output: False


6.def pattern_list_comprehension(n):
    for i in range(1, n + 1):
        print(' '.join(['*'] * i))

# Example usage
pattern_list_comprehension(4)


7.def triangle_list_comprehension(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join([str(x) for x in range(1, 2 * i)]))

# Example usage
triangle_list_comprehension(3)


8.def alphabet_pattern_list_comprehension(n):
    for i in range(1, n + 1):
        # Calculate spaces for the current row
        spaces = ' ' * (n - i) * 2
        
        # Create the alphabet sequence
        forward_seq = [chr(65 + j) for j in range(i)]  # A, B, C, ...
        backward_seq = forward_seq[:-1][::-1]  # A, B, ... and then reversed
        
        # Combine forward and backward sequence
        row = forward_seq + backward_seq
        
        # Print the row with spaces
        print(spaces + '   '.join(row))

# Example usage
alphabet_pattern_list_comprehension(3)
