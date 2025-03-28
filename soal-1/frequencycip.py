from collections import Counter

def analyze_ciphertext(ciphertext):
    ciphertext = ciphertext.replace(" ", "").replace("\n", "").upper()
    
    # Single letter frequency analysis
    freq = Counter(ciphertext)
    total_letters = sum(freq.values())
    freq_percent = {k: (v / total_letters) * 100 for k, v in freq.items()}
    
    # N-gram analysis (trigrams)
    trigrams = [ciphertext[i:i+3] for i in range(len(ciphertext)-2)]
    trigram_freq = Counter(trigrams)
    
    return freq_percent, trigram_freq

def print_frequency_analysis(freq_percent, trigram_freq):
    print("\nAnalisa Frekuensi:")
    print("+-------+-----------+")
    print("| Huruf| Frekuensi |")
    print("+-------+-----------+")
    for letter, percent in sorted(freq_percent.items(), key=lambda x: -x[1]):
        print(f"|   {letter}   |   {percent:.2f}%   |")
    print("+-------+-----------+")
    
    print("\nTop 10 Trigrams:")
    print("+---------+--------+")
    print("| Trigram | Frekuensi  |")
    print("+---------+--------+")
    for trigram, count in trigram_freq.most_common(10):
        print(f"|  {trigram}   |  {count:4}  |")
    print("+---------+--------+")

def main():
    # Get ciphertext from user input
    ciphertext = input("Masukkan Ciphertext: ")
    
    # Perform analysis
    freq_percent, trigram_freq = analyze_ciphertext(ciphertext)
    
    # Print results
    print_frequency_analysis(freq_percent, trigram_freq)

if __name__ == "__main__":
    main()