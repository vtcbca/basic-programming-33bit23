4.def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

# Example usage
print(reverse_string_recursive("hello"))  # Output: "olleh"