import numpy as np

def matrix_multiply_mod26(A, B):
    """
    Mengalikan dua matriks 3x3 lalu mengambil hasilnya mod 26.
    """
    # Pastikan matriks berbentuk 3x3
    if A.shape != (3, 3) or B.shape != (3, 3):
        raise ValueError("Matriks harus berukuran 3x3")
    
    # Perkalian matriks
    result = np.dot(A, B) % 26
    return result

# Contoh penggunaan
A = np.array([[ 6, 13, 20],
              [24, 16, 17],
              [ 1, 10, 15]])


B = np.array([[8, 21, 21],
              [5, 8, 12],
              [10, 21, 8]])


hasil = matrix_multiply_mod26(A, B)
print("Hasil perkalian matriks mod 26:")
print(hasil)
