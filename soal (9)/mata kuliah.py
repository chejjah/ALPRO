def main(): #F
    try: #F
        # Meminta pengguna memasukkan jumlah mata kuliah #F
        jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: ")) #F

        total_sks = 0 #F
        total_bobot = 0 #F

        for i in range(jumlah_mata_kuliah): #F
            # Meminta pengguna memasukkan nilai untuk setiap mata kuliah #F
            alpro = input(f"Masukkan nama mata kuliah ke-{i + 1}: ") #F
            sks = int(input(f"Masukkan jumlah SKS mata kuliah {i + 1}: ")) #F
            nilai = input(f"Masukkan nilai mata kuliah {i + 1} (A, B, C, atau D): ") #F

            # Menghitung bobot berdasarkan nilai #F
            bobot = hitung_bobot(nilai) #F

            # Menghitung total SKS dan total bobot #F
            total_sks += sks #F
            total_bobot += sks * bobot #F

        # Menghitung IPS #F
        ips = total_bobot / total_sks #F

        # Menampilkan hasil IPS #F
        print(f"Indeks Prestasi Semester (IPS): {ips:.2f}") #F

    except ValueError: #F
        print("Input tidak valid. Pastikan jumlah SKS berupa angka.") #F

def hitung_bobot(nilai): #F
    if nilai == 'A': #F
        return 4.0 #F
    elif nilai == 'B': #F
        return 3.0 #F
    elif nilai == 'C': #F
        return 2.0 #F
    elif nilai == 'D': #F
        return 1.0 #F
    else: #F
        return 0.0 #F

if __name__ == "__main__": #F
    main() #F