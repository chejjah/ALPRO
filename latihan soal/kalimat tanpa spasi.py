def hapus_spasi_berlebih(kalimat):
    # Menggunakan split() untuk membagi kata-kata dalam kalimat
    kata_kata = kalimat.split()

    # Menggunakan join() untuk menggabungkan kembali kata-kata dengan satu spasi sebagai pemisah
    kalimat_baru = " ".join(kata_kata)

    return kalimat_baru

# Input kalimat dengan spasi berlebih
kalimat = "saya tidak suka        memancing ikan    "
kalimat_tanpa_spasi_berlebih = hapus_spasi_berlebih(kalimat)

# Menampilkan hasil
print(kalimat_tanpa_spasi_berlebih)
