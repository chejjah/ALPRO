gaji = 10000
jam_kerja = 50
gaji_budi = gaji * jam_kerja 
print ("gaji budi selama 5 minggu: ", gaji_budi)

pajak1 = gaji_budi * 0.14
gaji_budi2 = gaji_budi - pajak1
print ("uang budi setelah pajak: ", gaji_budi2)

baju = gaji_budi2 * 0.1
gaji_budi3 = gaji_budi2 - baju 
print ("uang yang dihabiskan budi untuk baju dan aksesoris: ", baju)
print ("uang budi setelah beli baju: ", gaji_budi3)

alat_tulis = gaji_budi3 * 0.01
gaji_budi4 = gaji_budi3 - alat_tulis
print ("uang yang dihabiskan budi untuk lat tulis: ", alat_tulis)
print (" uang budi setelah beli alat tulis: ", gaji_budi4)

sedekah = gaji_budi4 * 0.25
yatim = sedekah * 0.3
dhuafa = sedekah - yatim 
gaji_budi5 = gaji_budi4 - sedekah 
print ("juamlah uang sedekah: ", sedekah)
print ("jumlah uang yang diberikan untuk yatim: ", yatim)
print ("jumlah uang yang diberikan untuk dhuafa: ", dhuafa)
print ("uang budi setelah sedekah: ", gaji_budi5)




       
