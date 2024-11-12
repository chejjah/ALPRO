sisi1 = 22
sisi2 = 22
sisi3 = 25
def main():
    try:
        # Meminta pengguna memasukkan panjang sisi-sisi segitiga
        sisi1 = float(input("Masukkan sisi 1: "))
        sisi2 = float(input("Masukkan sisi 2: "))
        sisi3 = float(input("Masukkan sisi 3: "))

        # Mengecek apakah sisi-sisi membentuk segitiga
        if is_valid_triangle(sisi1, sisi2, sisi3):
            if sisi1 == sisi2 == sisi3:
                print("3 sisi sama")
            elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
                print("2 sisi sama")
            else:
                print("Tidak ada yang sama")
        else:
            print("Sisi-sisi tidak membentuk segitiga.")

    except ValueError:
        print("Input tidak valid. Masukkan panjang sisi-sisi dalam bentuk angka.")

def is_valid_triangle(sisi1, sisi2, sisi3):
    # Kondisi untuk membentuk segitiga: jumlah dua sisi harus lebih besar dari sisi ketiga
    return sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1

if __name__ == "__main__":
    main()
