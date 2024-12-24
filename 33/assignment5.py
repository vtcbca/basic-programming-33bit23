
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
