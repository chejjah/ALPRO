# Pelanggan masuk dan diberi sambutan yang ramah
print("Selamat datang di Pizza Hut, ada yang bisa kami bantu?" )

# Menginformasikan kepada pelanggan terkait menu yang tersedia
print("""
Ini menu yang tersedia hari ini, silahkan pilih menu yang ada mau.
    Menu Pizza: 
      [1] Frankfurter
      [2] Meat Monsta
      [3] Super Supreme
      [4] Super Supreme Chicken
      """)
Pizza = int(input("Pizza yang ingin di pesan: "))

# Ukuran pizza yang diinginkan
print("""
Selanjutnya dilahkan pilih ukuran pizza yang anda mau
    Pilih ukuran:
      [A] Personal
      [B] Regular
      [C] Large
      """)
Ukuran = (input("Ukuran pizza yang anda pilih:"))

# Pilih pinggiran pizza
print("""
Lalu silhakan pilih pinggiran pizza anda
    Crust:
     [A] Pan
     [B] StuffedCrust Cheese
     [C] StuffedCrust Sausage
     [D] Cheese Bites
      """)
Crust = (input("Crust pizza yang anda pilih: "))

# Pilihan opsional untuk extra cheese
print("""Apakah anda ingin extra cheese atau tidak?
     [A] Dengan Extra Cheese
     [B] Tanpa Extra Cheese
      """)
Extra_cheese = input("Apakah anda ingin extra cheese? Y/N ")

# Code perintah untuk menjalankan pesanan secara otomatis
if Pizza in range (1, 4):

    # Harga Ukuran
    if Ukuran == "Personal":
        harga_ukuran = 43636
    elif Ukuran == "Regular":
        harga_ukuran = 100909
    else:
        harga_ukuran = 132727
    

    # Harga Crust
    if Crust == "Pan":
            harga_crust = 0
    elif Crust == "StuffedCrust Cheese":
            harga_crust = 11819
    elif Crust == "StuffedCrust Sausage":
            harga_crust = 9091
    else:
        harga_crust = 136371
    
        
    # Harga Extra Cheese
    if Extra_cheese == "Y":
        harga_extra_cheese = 13000
    else:
        harga_extra_cheese = 0
    
else:
     print("salah")

# Total harga dari pizza yang pelanggan pilih
total_harga = harga_ukuran + harga_crust + harga_extra_cheese
print(f"Terima kasih telah mempercayakan pesanan pizza anda pada kami. Ini total harga yang perlu anda bayarkan: Rp {total_harga},00")

# Metode pembayaran yang di pilih oleh pembeli
print ("""
Selanjutnya silahkan pilih metode pembayaran yang anda inginkan:
[1] Cash
[2] Transfer
""")
metode = input( "Pilih Kode Metode Pembayaran : ").lower()

if metode == "2":
    print("""
    Pilih Bank Tujuan
    [1] BCA 
    [2] BRI 
    [3] BNI 
    [4] BANK MEGA 
    [5] BTN 
    [6] CIMBNIAGA 
    [7] MANDIRI 
    [8] BANK JATIM 
    """)
    Bank = int(input("Masukkan Pilihan Bank : "))

    if Bank in range (1, 8):
        Rek = int(input("Masukkan Rekening : "))
        Nominal = int(input("Masukkan Nominal Transfer : "))
        Pin = int(input("Masukkan PIN : "))
        print("TRANSAKSI BERHASIL TERIMA KASIH TELAH BERBELANJA")
else:
    print("Silahkan Berikan Uang")

    
