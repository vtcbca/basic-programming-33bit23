7.def triangle_list_comprehension(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join([str(x) for x in range(1, 2 * i)]))

# Example usage
triangle_list_comprehension(3)