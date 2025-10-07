def min_max(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"{sequence} is not list or tuple")
    
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    
    min_val = sequence[0]
    max_val = sequence[0]
    
    for element in sequence:
        if element < min_val:
            min_val = element
        if element > max_val:
            max_val = element
    
    return (min_val, max_val)


def unique_sorted(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"{sequence} is not list or tuple")
    unique_elements = set(sequence)
    return sorted(unique_elements)


def flatten(matrix):
    if not isinstance(matrix, (list, tuple)):
        raise TypeError(f"{matrix} is not list or tuple")
    
    result = []
    
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"{row} is not list or tuple")
        
        for element in row:
            result.append(element)
    
    return result


print("=== min_max ===")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
try:
    print(min_max([]))
except ValueError as e:
    print("Error:", e)
print(min_max([1.5, 2, 2.0, -3.1]))

print("\n=== unique_sorted ===")
print(unique_sorted([3, 1, 2, 2, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("\n=== flatten ===")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], [3, 4, 5]]))
print(flatten([[1], [], [2, 3]]))
try:
    print(flatten([[1, 2], "ab"]))
except TypeError as e:
    print("Error:", e)
