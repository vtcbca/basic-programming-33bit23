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
