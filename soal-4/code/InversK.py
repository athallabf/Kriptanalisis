from sympy import Matrix, mod_inverse

# Given matrices
C = Matrix([
    [2, 2, 3],
    [3, 2, 10],
    [4, 25, 16]
])

P = Matrix([
    [7, 11, 24],
    [4, 14, 1],
    [11, 2, 4]
])

def matrix_mod_inv(matrix, mod):
    det = matrix.det() % mod
    if det == 0 or not mod_inverse(det, mod):
        raise ValueError(f"Matrix tidak dapat diinvers modulo {mod}")
    
    return (matrix.adjugate() * mod_inverse(det, mod)) % mod

# Hitung C⁻¹ mod 26
try:
    C_inv = matrix_mod_inv(C, 26)
except ValueError as e:
    print(e)
    exit()

# Hitung K⁻¹ = P * C⁻¹ mod 26
K_inv = (P * C_inv) % 26

# Tampilkan hasil
print("K⁻¹ =")
print(K_inv)
