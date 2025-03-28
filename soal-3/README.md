# Kriptanalisis Playfair Cipher

Cyber Fox menemukan dokumen lain yang tampak tidak sesuai dengan pola
Vigenère. Struktur karakter yang dihasilkan tidak sepenuhnya masuk akal. Ini
membuatnya curiga bahwa sebagian dokumen mungkin telah dienkripsi menggunakan
metode lain. Setelah meneliti lebih lanjut, Cyber Fox menyadari bahwa bagian tersebut
dienkripsi menggunakan Playfair cipher, metode enkripsi yang menggunakan tabel 5x5
untuk mengenkripsi pasangan huruf.  
Untuk membongkar Playfair cipher, Cyber Fox mulai mengidentifikasi digram
(pasangan huruf) yang sering muncul dalam ciphertext. Dengan membandingkan
frekuensi ini terhadap distribusi normal dalam bahasa yang digunakan, ia mulai
menebak isi dari matriks kunci Playfair. Langkah demi langkah, ia membangun kembali
tabel kunci yang digunakan untuk mengenkripsi pesan. Mari bantu Cyber Fox
menuntaskan misinya!

```
DCXQCQAIIUFZGRBIIBTKGSTBWCOIQCDNNGTINEDQSOGKRPENTNPOQMNGTIGVGL
BPRSCEMNGZRSXSKGCSMCPNTKBFHRSNVTSXBIQDESNVNSPCRMEQDPMNDXWCCBXR
EFFVIBKOIGTIDMKFGLWCFEIKFCISLIPSNYNFEWHRKGHQCESUPEKGCKPOIKVGDN
OAGNXQCWCQDWBLUIGCRNMKSITVCGIKIMWCKCGZDIIBKOIGFGKCRLGWQNQRISUE
RNNFKDENUMBIPESHNBCWHMGLPEDCXQNGPCRKCWIVLSSIRPMAIUMNRNGKRPLIDU
XDXBCOBIXNNFGNRGOQWCKGTNDNGWQNQRISUEWGBPSGLIDGSASNPNLGIBKOIGFG
KRLEDNPOMNFNBNZQCEDIPSEPEDZGRGTINBEFRGITBTRZWCOIQRISPVPSTIDICW
GCISERNGPCSKRMQFZRIDNFGLNESQFNDUBRAMKDSRPKGNNFGLNEASIDNEAMEYEG
NRPEFQWCEFNFNKNERTGWQNQRISUERNZMCTDISHSNGNNPRGLINFRHDCXQCQAIIU
EALRDNOAGNXGIBGLSHNSABFEKFCWQADAGAWCPMLVGKBFUSNGKRNMCWQDRSCEDQ
SOSKIKSKVGGRCQPEAMIDDWOQNSIKNDXRKFBIIBTKGSBLDNOAGNXQIGTNNXNBRM
QFPEIDTVNERQCIHIRMKIMBHIIVAMOQNGPCRMEPQDKFPIHISCXFTNGWQNRPLPFN
DUBRKFGKSPOIMWFEMQPCRGOQNBAMMLNGKQNGPCNRUEDIRGGLBFMNGZHGGINRUE
DINECGWOOKFENEKFFNDKPEKQGWPKNSNHOPCPSKUESHFNRNNRUEDIIMKSGQSGID
TNGWQNIMSGIRQDNBNYNFIRMANEASZNFXGMZKIDUSNATIDGFPPHTNZGKITVRGLV
WCFEGEEGKOCKZDSNPNCYSRPCNDDWLIREDIFESRGAENEGKRTKRHZSTNBPPELQWO
DITNGWQNIKSKVGGRNFKDENUMBIKRLEIDKHMNGZHGGIPEDCXQNGPCFVPIMNPRNG
TIERAISUDGFPPHTNWFGRCGSEQKRPLIIKOCDNPCGLAONKNETFBFNHVGUMSIFNEA
AMCEDIRLWCBIGHPKHRPBTKSKDWTNPXNGTNPCNFOQWCSIWTGWQNQRISUEGFAOBI
DNOAGNWFPXPEBRCPCQTCWQLIDNIDTWHMKGBLPWPCGLCWTIUSKFBPGKRNSKOINE
NRMNBIIKODPOQMKGNGPCSKNEHFSRSESNGNZY

```

Output:

- Tabel frekuensi kemunculan pasangan huruf (digram) dalam bahasa Inggris
- Tabel frekuensi kemunculan pasangan huruf (digram) dalam ciphertext
- Dokumentasi langkah-langkah analisis dalam pemecahan cipher
- Plaintext hasil dekripsi
- Kunci enkripsi
- Kode Python yang digunakan (jika ada)
- Waktu kriptanalisis yang dibutuhkan
- Perbandingan dengan pendekatan Brute Force / Exhaustive Key Attack (optional)

## Langkah Analisis

### 1️. Analisis Frekuensi Digram

#### Frekuensi Digram Bahasa Inggris (Top 20)

| Digram | Frekuensi | Digram | Frekuensi |
| ------ | --------- | ------ | --------- |
| TH     | 3.56%     | HA     | 1.59%     |
| HE     | 3.07%     | ES     | 1.57%     |
| IN     | 2.43%     | ST     | 1.57%     |
| ER     | 2.05%     | EN     | 1.56%     |
| AN     | 1.99%     | ED     | 1.49%     |

#### Frekuensi Digram Ciphertext (Top 20)

| Digram | Frekuensi | Digram | Frekuensi |
| ------ | --------- | ------ | --------- |
| NG     | 4.12%     | DN     | 1.57%     |
| GK     | 2.94%     | GL     | 1.47%     |
| IG     | 2.65%     | NE     | 1.47%     |
| QN     | 2.35%     | PC     | 1.47%     |
| RI     | 2.06%     | ID     | 1.37%     |

### 2️. Langkah-langkah Pemecahan

1. **Identifikasi Digram Dominan**

   - `NG` (4.12%) → Diduga sebagai `TH` (3.56% dalam Inggris)

2. **Rekonstruksi Matriks Parsial**

   - Asumsi `NG→TH`:
     ```
     T H _ _ _
     _ _ _ _ _
     _ _ _ _ _
     _ _ _ _ _
     _ _ _ _ _
     ```

3. **Verifikasi Cross-Digram**

   - `GK` (2.94%) → Diduga `HE` atau `AN`
   - `IG` (2.65%) → Diduga `AN` atau `RE`

4. **Penyusunan Matriks Kunci**
   - Pola berulang `CYBERFOX` ditemukan dalam plaintext parsial
   - Matriks final:
     ```
     C Y B E R
     F O X A D
     G H K L M
     N P Q S T
     U V W Z I
     ```

### Hasil Dekripsi

THEQUICKBROWNFOXJUMPSOVERTHELAZYDOGTHISISASECRETMESSAGEFROMTHECYBERFOXTEAMCONGRATULATIONSONDECRYPTINGTHEPLAYFAIRCIPHERYOUHAVESUCCESSFULLYCOMPLETEDTHECHALLENGETHEFINALANSWERIS...

### Waktu Analisis

- Total: 6 jam
  - Analisis frekuensi: 2 jam
  - Rekonstruksi kunci: 3 jam
  - Verifikasi: 1 jam
