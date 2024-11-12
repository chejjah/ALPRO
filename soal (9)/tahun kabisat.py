def cek_tahun_kabisat(tahun): #F
    if (tahun % 4 == 0): #F
        return True #F
    else: #F
        return False #F
    
# mengecek tahun dari 1900 hingga 2020 #F
for tahun in range(1900, 2021): #F
    if cek_tahun_kabisat(tahun):#F
        print(f"{tahun} adalah tahun kabisat")
    else: #F
        print(f"{tahun} bukan tahun kabisat")