# Membaca kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Memisahkan kata-kata dalam kalimat
kata_kalimat = kalimat.split()

# Inisialisasi kata terpendek dan terpanjang dengan kata pertama
kata_terpendek = kata_kalimat[0]
kata_terpanjang = kata_kalimat[0]

# Loop melalui kata-kata dalam kalimat untuk menemukan kata terpendek dan terpanjang
for kata in kata_kalimat:
    if len(kata) < len(kata_terpendek):
        kata_terpendek = kata
    elif len(kata) > len(kata_terpanjang):
        kata_terpanjang = kata

# Menampilkan hasil
print("Kata terpendek:", kata_terpendek)
print("Kata terpanjang:", kata_terpanjang)
