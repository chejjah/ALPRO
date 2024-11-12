def hitung_frekuensi_kata(kalimat, kata_dicari):
    # Menghitung frekuensi kemunculan kata_dicari dalam kalimat
    frekuensi = kalimat.count(kata_dicari)
    return frekuensi

# Input kalimat dan kata yang dicari
kalimat = "Saya mau mandi. Mandi tiga kali sehari. Jika tidak mandi badan akan bau"
kata_dicari = "mandi"

frekuensi = hitung_frekuensi_kata(kalimat, kata_dicari)
print(f"{kata_dicari} ada {frekuensi} buah")