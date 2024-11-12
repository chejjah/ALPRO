def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_closest_prime_less_than_n(n):
    if n <= 2:
        print("Tidak ada bilangan prima yang lebih kecil dari", n)
        return
    prime = n - 1 if n % 2 == 0 else n - 2
    while prime >= 2:
        if is_prime(prime):
            print("Bilangan prima terdekat yang lebih kecil dari", n, "adalah:", prime)
            return
        prime -= 2

try:
    n = int(input("Masukkan bilangan n: "))
    find_closest_prime_less_than_n(n)
except ValueError:
    print("Masukan harus berupa bilangan bulat.")
