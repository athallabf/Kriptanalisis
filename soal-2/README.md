Ciphertext:

```md!
UIGVTZGBSGPEPWAIKRKXUNIKDIWRETNCSWMMULRNAEOONQOBERBOOYWSLYQTCZMZMKQTGDYCLVUYIEICSEQTTPGBSCXGREOPVRQRYWIPWWWXBTLVAFVYOQPOGGTKWZRVVNQJEPNCMIQTGEHOKVKARTTIGWJUTSSDGIMJAYDDJRVYMTTDWULGTLCBQGBUGCAZZZKSENHKFZASSFNNWIXONPSCWEBOAWPBGKWIOWSZSIBOCFLKJCGZRLNCHFZZLLYOJJMIUCIDQKTYWSIMZWIIIWIDSKMYRZBEKKMTCCYZLZWTANRYKJVAMPRYMJIVPWIMSKQUNDHYOVDKROECHZBKIESCAXVOFTCKFTMIRJPDGXZGPSYSKZVNECEXLCGJEWIMSKMOTDSOULZOTJCKFSMKNEIBWCGIOXPBGDQYEOBISJQTGWENWJQMNQLKOFZIOOIXYDQYTLKOUFVBEYTSGEIRSZFDORZKTPSDAEOGPARYSTPKSDUMZRAANTTDWJBONRABWZVGDPQESKMLOCDOLVKZIYGFMCVKRLBSDZBOEDIXUIGVTZGBSGPOCDYCLVUYIYSDWRLZHPIBKVKARTTIAJDGLTDKLVLZHCOEYYZOGZRYMJUGTSEWSKQIAWAXSCGYIDAXVWWXMLLZJFWLSOEWGEAZRLTSFXIJHPROFTMZOPSCWEBOAWSOULZOTJPBAEKOPWECLYMYEARYGWAUFEEXVVXKNOOXJVIYOYALDVIYSFMZLZWTSEOCMSAZAYTSSKMZHPIBUCIOMDOXWFNZHPEKJCQKSEPYDPIRPSALWKQIEYCBQGBOOYTOUYVOQFECAJBNEGIQWEZKCTPRWILKVPLYHVLONEHOLYKKNEUBQLVRIVECADXREDULKKQZUEIYFTQVHPRCNZOKNCEOFTZEPEIYFVUVLZYCSIMVELTSFXSKYHOBVKWJEEEBEZVKLPTDWIANIQTCERSONRIDEFZKRPSSKKITTEOPJVYAEYCISEIRYDICXFZIEYTEJZMYIEWKKTWTSTDOJVLANMROSBIHLPDEWKWOTDCYEGTKXTTIUFUVACENLFUUNZAVHYIHEEIMUZXNECSRGNMBECIDAJVUWPACACGJENIZZVZKDFSSFXBKCSNSILMYSFCRSJBNEVACAJSOEIAWAEIZIZNYJWZKQFEXUPITAWYCAJWLRPPOSKQTGAADLVZTSTNDZVKOPSEBLVFZDPSZAKMOTDHSKKWXINAVADXUREAXUVBNEGIQWEZKCTPRWIVULZNQWIXXOGINWJIJEBUKLVAKCFRSLPPOGSLSYYBONRAUWPXXIYCSHCMONXONWIVIRJPDGXZGPSYDJLMVRZTOUKQUNCEVAVATOEOXDPWTSPCBWTGHUEAVKFWTSERYFXUGTSEWSKQIAWFYMELGTTOXKRVJCZMZMKIZIZNKDZVLELSSTZTOTJ
```



![image](https://hackmd.io/_uploads/HkpDfJ4pkl.png)


KEY: SRIGALAK

Langkah-langkah:
1. masukkan decrypted text pada bagian `Intercept` di website {%preview https://crypto.interactive-maths.com/kasiski-analysis-breaking-the-code.html %} 
2. ![image](https://hackmd.io/_uploads/SywaLJVake.png)

3. Lalu kita lihat dari tabel sequence untuk mencari berapa jumlah huruf pada key
![image](https://hackmd.io/_uploads/rkeX-1Ep1g.png)
![image](https://hackmd.io/_uploads/Bk2CZJVTJl.png)
Tabel ini menunjukkan huruf yang muncul dua kali dengan jarak antara keduanya.
Misalkan yang pertama yaitu WIMS terdapat angka 64 disebelahnya, berarti dia muncul 2 kali dengan jarak 64 huruf diantaranya, lalu disampingnya yaitu tabel angka 2,3,4, dst adalah yang merupakan faktor-faktor dari 64.

Untuk mencari panjang huruf dari key, kita lihat faktor yang paling besar dengan jumlah yang paling banyak, dalam hal ini faktor 64 ada 2,3 dan 8 (bisa dilihat dari kotak hijau paling panjang). Berarti panjang key adalah 8 (terbesar) setelah itu kita masukkan ke keyword finder:
![image](https://hackmd.io/_uploads/r1ubE1V6Je.png)
Lalu untuk masing-masing keyword, kita lakukan shift agar diagram merah dan biru bisa match (tidak harus match banget asalkan lumayan match, karena disini kita memperkirakan). Contoh disini untuk key pertama dengan diagram biru merah paling match adalah huruf S 
![image](https://hackmd.io/_uploads/rkaOEkEp1e.png)
Lakukan hal yang sama untuk keyword berikutnya.

Misalkan ketika sudah kita lakukan sampai keyword terakhir lalu dia belum match, contoh:
![image](https://hackmd.io/_uploads/rJ67HyNpyg.png)

Maka kita bisa cari kira-kira huruf mana yang perlu diubah, bisa dilihat di bagian awal
`cryltograph` seharusnya adalah `cryptograph`
maka kita coba shifting lagi key yang bisa mengubah `cryltograph` menjadi `cryptograph`

![image](https://hackmd.io/_uploads/S11AHyV6Jl.png)
Key ke-4 yang awalnya K diubah menjadi G
![image](https://hackmd.io/_uploads/Hk1jry46Jx.png)
sehingga decrypted text menjadi
![image](https://hackmd.io/_uploads/HkD3ryEa1g.png)

Dapat plaintextnya:
```md!
cryptographyplaysacrucialroleinsafeguardinginformationwithincomputingsystemsitisanintegralpartofdailylifeforbillionsofpeopleworldwideensuringthesecurityofbothstoredandtransmitteddatacryptographicmechanismsunderpinessentialprotocolsparticularlytransportlayersecuritytlswhichfacilitatesrobustencryptionacrossnumerousapplicationshoweverdespiteitssignificancecryptographyisinherentlydelicateitssecuritycanbeentirelycompromisedbyasingledesignflaworcodingmistakeconventionalsoftwaretestingapproachessuchasunittestingareinadequatefordetectingvulnerabilitiesincryptographicsystemsinsteadtheirsecurityisvalidatedthroughrigorousmathematicalanalysisandformalproofsdemonstratingadherencetoessentialsecurityprinciplestheseproofsoftendependonreasonableassumptionstosubstantiatetheirclaimsoneoftheearliestpolyalphabeticencryptiontechniquesisthevigenrecipherdevelopedinthethcenturyunlikesimplesubstitutionciphersvigenreencryptionemploysarepeatingkeywordtodeterminelettershiftsmakingitmoreresistanttofrequencyanalysisforcenturiesitwasconsideredunbreakableduetoitscomplexitycomparedtomonoalphabeticciphershoweveritisnoweasilydecipheredusingtechniquessuchasthekasiskiexaminationorfrequencyanalysisofrepeatingpatternsintheciphertextdespiteitshistoricalimportancethevigenreciphernolongerprovidesadequatesecurityhighlightingakeyprincipleinmoderncryptographytrueprotectionreliesnotonlyonsecrecybutalsoonstrongmathematicalfoundationsandcomputationalinfeasibility
```

kita minta ChatGPT untuk memberi spasi agar lebih mudah dibaca:
```md!
Cryptography plays a crucial role in safeguarding information within computing systems. It is an integral part of daily life for billions of people worldwide, ensuring the security of both stored and transmitted data. Cryptographic mechanisms underpin essential protocols, particularly Transport Layer Security (TLS), which facilitates robust encryption across numerous applications. However, despite its significance, cryptography is inherently delicate. Its security can be entirely compromised by a single design flaw or coding mistake. Conventional software testing approaches, such as unit testing, are inadequate for detecting vulnerabilities in cryptographic systems. Instead, their security is validated through rigorous mathematical analysis and formal proofs demonstrating adherence to essential security principles. These proofs often depend on reasonable assumptions to substantiate their claims. One of the earliest polyalphabetic encryption techniques is the Vigenère cipher, developed in the 16th century. Unlike simple substitution ciphers, Vigenère encryption employs a repeating keyword to determine letter shifts, making it more resistant to frequency analysis. For centuries, it was considered unbreakable due to its complexity compared to monoalphabetic ciphers. However, it is now easily deciphered using techniques such as the Kasiski examination or frequency analysis of repeating patterns in the ciphertext. Despite its historical importance, the Vigenère cipher no longer provides adequate security, highlighting a key principle in modern cryptography: true protection relies not only on secrecy but also on strong mathematical foundations and computational infeasibility.
```

Selesai