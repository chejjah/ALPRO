tinggi = 5
lebar = 4
def print_pattern(tinggi, lebar):
    start = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(start, end=" ")
            start += 1
        print()

# menggunakan input dari pengguna
tinggi = int(input("masukkan tinggi: "))
lebar = int(input("masukkan lebar: "))

print_pattern(tinggi, lebar)
