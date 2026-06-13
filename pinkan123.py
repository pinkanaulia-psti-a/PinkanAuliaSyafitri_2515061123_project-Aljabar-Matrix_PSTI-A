def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("ukuran kedua vektor harus sama")

    hasil = 0
    for i in range(len(a)):
        hasil += a[i] * b[i]

    return hasil


def transpose(matrix):
    baris = len(matrix)
    kolom = len(matrix[0])

    hasil = []
    for j in range(kolom):
        baris_baru = []
        for i in range(baris):
            baris_baru.append(matrix[i][j])
        hasil.append(baris_baru)

    return hasil


def hadamard_product(A, B):
    baris = len(A)
    kolom = len(A[0])

    if len(B) != baris or len(B[0]) != kolom:
        raise ValueError("ukuran matriks A dan B harus sama")

    hasil = []
    for i in range(baris):
        baris_baru = []
        for j in range(kolom):
            baris_baru.append(A[i][j] * B[i][j])
        hasil.append(baris_baru)

    return hasil


if __name__ == "__main__":
    vektor_a = [1, 2, 3]
    vektor_b = [4, 5, 6]
    print("Dot Product:", dot_product(vektor_a, vektor_b))

    matrix_c = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Transpose:", transpose(matrix_c))

    matrix_d = [
        [1, 2],
        [3, 4]
    ]
    matrix_e = [
        [5, 6],
        [7, 8]
    ]
    print("Hadamard Product:", hadamard_product(matrix_d, matrix_e))
