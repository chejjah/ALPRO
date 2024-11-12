def cek_digit_belakang (a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    
    if (digit_a == digit_b == digit_c) or (digit_a == digit_b) or (digit_a == digit_c) or (digit_b == digit_c):
        return True
    else:
        return False
    
bilangan_1 = int(input("masukkan bilangan 1: "))
bilangan_2 = int(input("masukkan bilangan 2: "))
bilangan_3 = int(input("masukkan bilangan 3: "))

hasil = cek_digit_belakang(bilangan_1, bilangan_2, bilangan_3)

if hasil:
    print("True")
else:
    print("False")
