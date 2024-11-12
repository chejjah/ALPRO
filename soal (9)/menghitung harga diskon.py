# Harga-harga barang
harga_cpu = 700000
harga_ram = 380000
harga_motherboard = 800000

# Hitung total harga pembelian
total_harga_pembelian = harga_cpu + harga_ram + harga_motherboard

# Periksa apakah total harga pembelian lebih besar dari 1.500.000,-
if total_harga_pembelian > 1500000:
    # Hitung diskon
    diskon = 0.10 * total_harga_pembelian
else:
    diskon = 0

# Hitung harga yang harus dibayar setelah diskon
harga_setelah_diskon = total_harga_pembelian - diskon

# Tampilkan total harga pembelian, diskon, dan harga setelah diskon
print("Total harga pembelian:", total_harga_pembelian)
print("Diskon:", diskon)
print("Harga setelah diskon:", harga_setelah_diskon)
