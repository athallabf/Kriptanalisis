import time

def decrypt_affine_image(input_path, output_path, m, b, n):
    start_time = time.time()
    
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
        # Dekripsi setiap byte
        decrypted_byte = (m_inv * (byte - b)) % n
        decrypted_data.append(decrypted_byte)
    
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
    
    end_time = time.time()
    decryption_time = end_time - start_time
    
    print(f"Waktu Dekripsi Gambar: {decryption_time:.6f} detik")

# Gunakan fungsi dekripsi (sesuaikan path)
decrypt_affine_image('affinecipher.jpeg', 'decrypted_image.jpg', 115, 42, 256)