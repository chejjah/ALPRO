
def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("masukkan nilai n: "))
if n <= 0:
        print("masukkan n yang lebih besar dari 0")
else: 
        print(f"nilai fibonacci ke-{n} adalah {fibonacci(n)}")