def main():
    try:
        # Meminta pengguna memasukkan nomor bulan (1-12)
        bulan = int(input("Masukkan nomor bulan (1-12): "))

        # Mengecek apakah nomor bulan valid (antara 1 dan 12)
        if 1 <= bulan <= 12:
            # Menentukan jumlah hari dalam bulan
            jumlah_hari = hitung_jumlah_hari(bulan)

            # Menampilkan hasil
            print(f"Jumlah hari dalam bulan {bulan} adalah {jumlah_hari}.")
        else:
            print("Nomor bulan tidak valid. Masukkan nomor bulan antara 1 dan 12.")

    except ValueError:
        print("Input tidak valid. Masukkan nomor bulan dalam bentuk angka.")

def hitung_jumlah_hari(bulan):
    # Daftar jumlah hari dalam setiap bulan di tahun 2020
    jumlah_hari_per_bulan = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Mengembalikan jumlah hari berdasarkan nomor bulan
    return jumlah_hari_per_bulan[bulan - 1]

if __name__ == "__main__":
    main()