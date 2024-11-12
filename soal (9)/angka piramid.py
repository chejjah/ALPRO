def print_series(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

try:
    n = int(input("Masukkan nilai n: "))
    for i in range(n, 1, -1):
        result = 1
        for j in range(i, 0, -1):
            result *= j
        print(result, end=" ")
        print_series(i - 1)
except ValueError:
    print("Masukan harus berupa bilangan bulat.")

