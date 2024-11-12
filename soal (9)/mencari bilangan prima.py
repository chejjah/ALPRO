def is_prime(num): 
    if num < 2: 
        return False  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0: 
            return False 
        return True 
    
N = int(input("Masukkan nilai N: ")) 

if N < 2: 
    print("tidak ada bilangan prima dalam rentang 1 sampai", N)
else: 
    print("bilangan prima dari 1 sampai", N, "adalah:")

    num = 2 
    while num <= N: 
        if is_prime(num): 
            print(num, end=", ")
        num += 1 

    print() # untuk memberikan baris baru setelah deret bilangan prima

    