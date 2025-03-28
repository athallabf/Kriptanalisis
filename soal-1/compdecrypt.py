import time
from collections import deque

def caesar_decrypt_bruteforce(ciphertext):
    """Dekripsi Caesar Cipher dengan mencoba semua kemungkinan shift (0-25)"""
    results = []
    for shift in range(26):
        result = []
        for char in ciphertext:
            if char.isupper():
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            elif char.islower():
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                result.append(char)
        results.append(f"Key: {shift:2} | Pesan: {''.join(result)}")
    return results

def caesar_decrypt_direct(ciphertext, key):
    """Dekripsi Caesar Cipher dengan key tertentu"""
    result = []
    key = key % 26
    upper_a, lower_a = ord('A'), ord('a')
    
    for char in ciphertext:
        if char.isupper():
            result.append(chr((ord(char) - upper_a - key) % 26 + upper_a))
        elif char.islower():
            result.append(chr((ord(char) - lower_a - key) % 26 + lower_a))
        else:
            result.append(char)
    return ''.join(result)

def main():
    print("=== Program Dekripsi Caesar Cipher ===")
    ciphertext = input("Masukkan ciphertext: ")
    
    # Mode brute-force
    print("\n[Metode Brute-Force]")
    start_time = time.time()
    brute_results = caesar_decrypt_bruteforce(ciphertext)
    brute_time = time.time() - start_time
    
    for result in brute_results:
        print(result)
    
    # Mode direct decryption
    print("\n[Metode Dekripsi Langsung]")
    try:
        key = int(input("Masukkan key (0-25): "))
        start_time = time.time()
        decrypted = caesar_decrypt_direct(ciphertext, key)
        direct_time = time.time() - start_time
        
        print(f"Hasil dekripsi: {decrypted}")
        
        # Perbandingan waktu eksekusi
        print("\n=== Perbandingan Waktu Eksekusi ===")
        print(f"Brute-force: {brute_time:.6f} detik")
        print(f"Dekripsi langsung: {direct_time:.6f} detik")
        print(f"Perbedaan: {abs(brute_time - direct_time):.6f} detik")
        
    except ValueError:
        print("Error: Key harus berupa angka!")

if __name__ == "__main__":
    main()