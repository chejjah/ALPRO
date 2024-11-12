def adalah_anagram(kata1, kata2):
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Mengecek panjang kata, jika berbeda, bukan anagram
    if len(kata1) != len(kata2):
        return False

    # Menghitung jumlah kemunculan setiap huruf di kedua kata
    char_count1 = {}
    char_count2 = {}

    for char in kata1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in kata2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Membandingkan jumlah kemunculan setiap huruf di kedua kata
    return char_count1 == char_count2

# Menggunakan program untuk menguji apakah dua kata adalah anagram
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if adalah_anagram(kata1, kata2):
    print(f"{kata1} dan {kata2} adalah anagram.")
else:
    print(f"{kata1} dan {kata2} bukan anagram.")