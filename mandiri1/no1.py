# Fungsi untuk menentukan apakah suatu tahun merupakan tahun kabisat atau bukan
def isKabisat(tahun):
    
    # Tahun kabisat jika:
    # 1. Habis dibagi 4 dan tidak habis dibagi 100
    # atau
    # 2. Habis dibagi 400
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True   # Mengembalikan nilai True jika tahun kabisat
    else:
        return False  # Mengembalikan nilai False jika bukan tahun kabisat


# Meminta input tahun dari user
tahun = int(input("Masukkan tahun: "))

# Memanggil fungsi isKabisat untuk mengecek apakah tahun tersebut kabisat
hasil = isKabisat(tahun)

# Menampilkan hasil pengecekan
print("Apakah tahun tersebut kabisat?", hasil)