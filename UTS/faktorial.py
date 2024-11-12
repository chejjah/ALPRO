def hitung_faktorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

n = int(input("masukkan angka: "))
hasil_faktorial = hitung_faktorial (n)
print(f"{n}! = {hasil_faktorial}")
