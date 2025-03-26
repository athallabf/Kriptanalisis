import time
import math

def find_affine_key(p1, c1, p2, c2, n):
    start_time = time.time()
    
    # Mencari invers modular
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    # Mencari perbedaan
    diff_p = (p1 - p2) % n
    diff_c = (c1 - c2) % n

    # Cari m (slope)
    m_inv = mod_inverse(diff_p, n)
    if m_inv is None:
        return None

    m = (diff_c * m_inv) % n

    # Cari b (intercept)
    b = (c1 - (m * p1)) % n

    end_time = time.time()
    
    # Waktu eksekusi
    execution_time = end_time - start_time
    
    return m, b, execution_time

# Fungsi Brute Force untuk perbandingan
def brute_force_key_search(p1, c1, p2, c2, n):
    start_time = time.time()
    
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    possible_keys = []
    
    for m in range(1, n):
        # Pastikan m dan n coprime
        if math.gcd(m, n) != 1:
            continue
        
        m_inv = mod_inverse(m, n)
        if m_inv is None:
            continue
        
        # Hitung b
        b = (c1 - (m * p1)) % n
        
        # Verifikasi kunci
        if ((m * p1 + b) % n == c1) and ((m * p2 + b) % n == c2):
            possible_keys.append((m, b))
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return possible_keys, execution_time

# Parameter
n = 256
p1, c1 = 0xFF, 0xB7
p2, c2 = 0xD8, 0x32

# Metode Analisis Pasangan Plaintext-Ciphertext
m, b, targeted_time = find_affine_key(p1, c1, p2, c2, n)
print(f"Kunci m (Targeted Search): {m}")
print(f"Kunci b (Targeted Search): {b}")
print(f"Waktu Kriptanalisis Terarah: {targeted_time:.6f} detik")

# Metode Brute Force
possible_keys, brute_force_time = brute_force_key_search(p1, c1, p2, c2, n)
print(f"\nBrute Force Hasil:")
print(f"Kunci yang Mungkin: {possible_keys}")
print(f"Waktu Brute Force: {brute_force_time:.6f} detik")

# Perbandingan Efisiensi
print(f"\nPerbandingan Waktu:")
print(f"Kriptanalisis Terarah: {targeted_time:.6f} detik")
print(f"Brute Force: {brute_force_time:.6f} detik")
print(f"Perbedaan: {abs(brute_force_time - targeted_time):.6f} detik")