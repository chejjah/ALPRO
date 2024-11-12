def palindrom(kalimat):
    #cek apakah kalimat adalah palindrom
    return kalimat == kalimat [::-1]

kalimat = input("masukkan sebuah kalimat: ")

if palindrom(kalimat):
    print("kalimat tersebut adalah palindrom")
else:
    print("kalimat tersebut bukan palindrom")
