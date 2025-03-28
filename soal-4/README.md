# Kriptanalisis Hill Cipher

Cyber Fox menemukan dokumen lain yang tampaknya memiliki struktur matriks
yang lebih kompleks. Pola dalam ciphertext tidak mengikuti sifat substitusi sederhana
maupun poli-alfabetik seperti sebelumnya. Cyber Fox menyadari bahwa Hill
Cipher telah digunakan untuk mengenkripsi bagian ini!
Jika frasa pertama yang diketahui adalah "Hello Cyber Fox, attacker here!",
Cyber Fox menggunakan known-plaintext attack (KPA) untuk menganalisis Hill
Cipher. Dengan teknik invers matriks modular, ia berusaha mengungkap kunci enkripsi
yang digunakan. Bantulah Cyber Fox membongkar pesan ini!

```
CDECCZDKQFYRYRWYWXKVTSBQABTRVRITRXVVKWKJKEMUEVKLYUPUAFSPPSFSKZ
VGJKKNLWNFXSMUDVHKSWMFERVUWEVZTZQVOGWALCAYTKXAKNKYDTZMTWATADAL
YSANZSBMIGPUGNTMHFJRSKSTLQKFRXAKHMOHEYQDUMSFIAMOBSKBFWZKGZEVAK
SHQHPGJUKKLNSZAIFCWUKUKWMMJUDVVOWHWXEAVWODIAMOBSDNNNUYYRVRWMPQ
PYJDZRXDZBJUKOPUXIZQTHSKKHEYATYCONMHOACPMNIESNKZZYBKTZHXCGOABR
EJCIDCJCRVRWNFCJPCUWYNQGCGSLJDWLCHBWNFLCMGNNTDLMPTLSYFWAUMGWFM
WQCCWPLAMTSZXAULWDEADALPBQIDUTSJGSWPGKBIAMOBSOKSPGFBDDLMECGVUD
VEEZYCORCJEIOMXENEQUMGZHUUSOSCNSFSMDPALWXAHIDEWNFJOQJLLELRNAUV
OQQDUINZIKVMSSSGOMGRHSKZWJVOQASVCKVIZGIQWPIQGJKLWURYLIQBOAZMHO
ACPMNIESNCUKXWSGIYEBHTYIBEIMHOACPMNIESNSKKHEYOOPTSOFRFHSGBZHXC
XATDOOFNOEWKQXHJYCUYUZBPXSMDESDJDOZGANUGMFWSMMLMCYZEVECXLFNUAC
WPYMHOBSWQCQWROHPVUMDOTEMXBGDANZKNUCSLFSKPCJUGAURCOQZOUEXTFWNF
ETPUPLZMTAVZQOZCJCRVRWNFYILHSXUSQBXBNSIFSFCWPHAVOHVWCRTNPIWQWL
YTEEEQXEMXBUPCAFBXBPGMPGVTFDTDLNGOCPMPUYXHWVZNMVDMZGOZDGQHSGWA
QXLZGPGSYUZAPVSBQBXBPGMPGVTFDVGGAWQOPAAVZDSSNLJANNSETBGXSSBFCJ
DWLCHBWNFMULCJCRVRNWJIUIFFVBVLHYCKKSTRZPQICAQUUPEKMEYLECLAHACA
SRIADDUVDHIQWZAIORLZMCAIEOMJNGONEDVCCOGXQMPXHJYCUYUZJOQDTJMXFW
QCEQXQJOMJPOJIABTRVRPUYEDSDDHSUOFIUTQJFESFWGATDZQVZVHBHZAPVSBQ
CBOXUNFQGZZPKSQQDUWUTGYNXLXFYEVZAYRFLAMDUNZUMPVDZZDMETGIVHMDNH
XAXPLLNCAYNSVDNAXSMVVLYDTCRPLRFLAMTSZXAULWDHCVAKKOHPVUMKJOSQGQ
BWYKLKRQSKKMMJLWWWTCYKEUGNWBGKNLWUTRYYYBLOIDNWREQXACLBEVUDVDEC
EQXMFWFRFUMONGIENMOEY
```

Output:
- Dokumentasi langkah-langkah analisis dalam pemecahan cipher
- Plainteks hasil dekripsi
- Matriks Kunci
- Matriks Invers Kunci
- Kode Python yang digunakan (jika ada)
- Waktu kriptanalisis yang dibutuhkan
- Perbandingan dengan pendekatan Brute Force / Exhaustive Key Attack (optional)

## Langkah analisis

1. Cari m <br/>
- Check jumlah huruf pada cipher text<br/>
![Check jumlah karakter](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img1.png)

https://charactercalculator.com/id/
Terdapat 1323 Karakter <br/>
- Check faktorisasi prima
![Faktorisasi Prima](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img2.png)

Kemungkinan m = 1, 3 karena 7^2 = 49 jumlah karakter pada plaintext tidak mencukupi maka m >=7 tidak memenuhi <br/>
2. Coba m=3 <br/>
```
Hello Cyber Fox, attacker here!
```
- Hilangkan spasi dan tanda baca<br/>
```
HelloCyberFoxattackerhere
```
- Ambil 9 karakter
```
HelloCybe
```
- Ambil 9 karakter dari cipher text
```
CDECCZDKQ
```
- Ubah menjadi numerik A=0 dst
```
p = 7 4 11 11 14 2 24 1 4
C = 2 3 4 2 2 25 3 10 16

P=
7 11 24 
4 14 1
11 2 4

C=
2 2 3 
3 2 10
4 25 16
```

3. Hitung K
Rumus
```
K = CP^-1 mod 26
```
Gunakan python
```
from sympy import Matrix

# Definisi matriks C dan P
C = Matrix([[2, 2, 3],
            [3, 2, 10],
            [4, 25, 16]])

P = Matrix([[7, 11, 24],
            [4, 14, 1],
            [11, 2, 4]])

# Hitung invers P dalam mod 26
try:
    P_inv_mod26 = P.inv_mod(26)
    # Hitung K = C * P^-1 mod 26
    K = (C * P_inv_mod26) % 26
except ValueError:
    P_inv_mod26 = "Matriks P tidak memiliki invers dalam mod 26"
    K = None

P_inv_mod26, K
```
## Matriks K
Didapatkan K

![Matriks K](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img3.png)

Gunakan Decoder Hill cipher online <br/>
![Matriks K](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img4.png)

https://www.dcode.fr/hill-cipher

Hasilnya terlihat masuk akal
## Plaintext hasil dekripsi 
![Hasil](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img5.png)

Berikut plaintext lengkapnya
```
HELLOCYBERFOXATTACKERHERECRYPTOGRAPHYISCRUCIALFORSAFEGUARDINGI NFORMATIONINCOMPUTINGSYSTEMSANDPLAYSANINTEGRALROLEINTHEDAILYLI VESOFBILLIONSOFPEOPLEWORLDWIDEBYENSURINGTHESECURITYOFBOTHSTORE DANDTRANSMITTEDDATAASACORECOMPONENTOFMANYSECURITYPROTOCOLSPART ICULARLYTRANSPORTLAYERSECURITYTLSCRYPTOGRAPHICMETHODSPROVIDEST RONGENCRYPTIONACROSSVARIOUSAPPLICATIONSHOWEVERDESPITEITSSIGNIF ICANCECRYPTOGRAPHYREMAINSVULNERABLEITSSECURITYCANBEENTIRELYCOM PROMISEDBYASINGLEDESIGNFLAWORCODINGERRORTRADITIONALSOFTWARETES TINGTECHNIQUESSUCHASUNITTESTINGAREINADEQUATEFORIDENTIFYINGCRYP TOGRAPHICWEAKNESSESINSTEADCRYPTOGRAPHICSECURITYISREINFORCEDTHR OUGHRIGOROUSMATHEMATICALPROOFSANDFORMALANALYSISTOVERIFYADHEREN CETOCRITICALSECURITYPRINCIPLESOFTENBASEDONREASONABLEASSUMPTION SONEOFTHEEARLYENCRYPTIONTECHNIQUESTHATADVANCEDBEYONDSIMPLESUBS TITUTIONCIPHERSISTHEHILLCIPHERDEVELOPEDINTHETHCENTURYUNLIKEMON OALPHABETICCIPHERSTHEHILLCIPHERUSESLINEARALGEBRAANDMATRIXMULTI
PLICATIONTOENCRYPTBLOCKSOFLETTERSSIMULTANEOUSLYMAKINGITMORERES ISTANTTOFREQUENCYANALYSISHOWEVERDESPITEITSMATHEMATICALSOPHISTI CATIONITCANBEDECRYPTEDIFANATTACKEROBTAINSENOUGHPLAINTEXTCIPHER TEXTPAIRSALLOWINGTHEMTOSOLVEFORTHEENCRYPTIONMATRIXTHISHIGHLIGH TSAFUNDAMENTALPRINCIPLEINMODERNCRYPTOGRAPHYTRUESECURITYRELIESN OTJUSTONSECRECYBUTALSOONSOLIDMATHEMATICALFOUNDATIONSANDCOMPUTA TIONALINFEASIBILITYAA
```
## Matriks Invers K
Gunakan code python
```
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

```
Matrix([ [ 8, 21, 21], 
[ 5, 8, 12], 
[10, 21, 8]])

Cek K x K^-1 
```
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
```
Hasilnya
```
Hasil perkalian matriks mod 26:
[[1 0 0]
 [0 1 0]
 [0 0 1]]
```
Kemudian kita cek menggunakan tools online `https://www.dcode.fr/hill-cipher`

cara kerja tools nya <br/>
- decript <br/>
```
cipher -> plaintext
key

p-> c
key-1 
```
- encrypt
```
p-> c
key

c-> p
key-1
```
![Img6](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img6.jpg) <br/>
![Img7](https://github.com/athallabf/Kriptanalisis/blob/main/soal-4/img/img7.jpg) <br/>
## Waktu Kriptanalisis
2 Jam

## Brute force
Exhaustive attacks are only a threat for small 𝑚
- Only feasible for small m 
Total invertible matrices modulo 26 = 157,248.
157,248 keys can be tested in seconds with modern computing (e.g., 1 millio keys/second).
- For 𝑚=3, ~10^12 keys: computationally impossible.
