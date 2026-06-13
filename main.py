import pinkan123

vektor_a = [1, 2, 3]
vektor_b = [4, 5, 6]
print("Dot Product:", pinkan123.dot_product(vektor_a, vektor_b))

matrix_c = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Transpose:", pinkan123.transpose(matrix_c))

matrix_d = [
    [1, 2],
    [3, 4]
]
matrix_e = [
    [5, 6],
    [7, 8]
]
print("Hadamard Product:", pinkan123.hadamard_product(matrix_d, matrix_e))
