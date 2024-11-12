def hitung_frekuensi_kata(kalimat, kata_dicari):
    # Mengonversi kalimat menjadi huruf kecil agar pencarian bersifat case-insensitive
    kalimat = kalimat.lower()
    kata_dicari = kata_dicari.lower()

    # Menghitung frekuensi kemunculan kata_dicari dalam kalimat
    frekuensi = kalimat.count(kata_dicari)

    return frekuensi

# Input kalimat dan kata yang dicari
kalimat = "Saya mau makan. Mandi tiga kali sehari. Jika tidak mandi badan akan bau"
kata_dicari = "mandi"

# Memanggil fungsi hitung_frekuensi_kata
frekuensi = hitung_frekuensi_kata(kalimat, kata_dicari)

# Menampilkan hasil
print(f"{kata_dicari} ada {frekuensi} buah")