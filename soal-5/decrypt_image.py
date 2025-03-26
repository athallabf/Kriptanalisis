def find_affine_key(p1, c1, p2, c2, n):
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

    return m, b

# Parameter
n = 256
p1, c1 = 0xFF, 0xB7
p2, c2 = 0xD8, 0x32

m, b = find_affine_key(p1, c1, p2, c2, n)

def decrypt_affine_image(input_path, output_path, m, b, n):
    # Cari invers modular m
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    m_inv = mod_inverse(m, n)
    
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = bytearray()
    for byte in encrypted_data:

        # Konversi byte ke integer jika perlu
        byte = ord(byte) if isinstance(byte, str) else byte
        # Dekripsi setiap byte
        decrypted_byte = (m_inv * (byte - b)) % n
        decrypted_data.append(decrypted_byte)
    
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

# Gunakan fungsi dekripsi
decrypt_affine_image('affinecipher.jpeg', 'decrypted_image.jpg', m, b, 256)