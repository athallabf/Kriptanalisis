# Mengimpor kembali pustaka yang diperlukan setelah reset
from sympy import Matrix

# Definisi matriks K
K = Matrix([[6, 13, 20],
            [24, 16, 17],
            [1, 10, 15]])

# Menghitung invers K dalam mod 26
try:
    K_inv_mod26 = K.inv_mod(26)
except ValueError:
    K_inv_mod26 = "Matriks K tidak memiliki invers dalam mod 26"

K_inv_mod26