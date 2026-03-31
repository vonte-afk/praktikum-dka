import numpy as np  # import library numpy untuk array

# list untuk menyimpan nama mahasiswa
nama_mahasiswa = []

# array numpy untuk menyimpan nilai (tugas, uts, uas)
nilai_array = np.array([])

# fungsi input data mahasiswa
def input_data():
    global nilai_array  # supaya bisa diubah di luar fungsi
    n = int(input("Masukkan jumlah mahasiswa: "))
    data = []  # list sementara untuk nilai

    for i in range(n):
        nama = input(f"Nama mahasiswa ke-{i+1}: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))

        nama_mahasiswa.append(nama)  # simpan nama
        data.append([tugas, uts, uas])  # simpan nilai dalam list

    nilai_array = np.array(data)  # ubah list ke numpy array

# fungsi menampilkan array nilai
def tampilkan_array():
    print("\nArray Nilai:")
    print(nilai_array)

# fungsi menghitung nilai akhir
def hitung_nilai_akhir():
    # rumus: 30% tugas + 30% uts + 40% uas
    return (0.3 * nilai_array[:,0]) + (0.3 * nilai_array[:,1]) + (0.4 * nilai_array[:,2])

# fungsi menampilkan nilai akhir
def tampilkan_nilai_akhir():
    nilai_akhir = hitung_nilai_akhir()
    for i, nilai in enumerate(nilai_akhir):
        print(f"{nama_mahasiswa[i]} = {nilai:.2f}")

# fungsi analisis kelas
def analisis_kelas():
    nilai_akhir = hitung_nilai_akhir()
    
    rata = np.mean(nilai_akhir)  # hitung rata-rata
    median = np.median(nilai_akhir)  # hitung median

    print(f"Rata-rata: {rata:.2f}")
    print(f"Median: {median:.2f}")

    print("Mahasiswa dengan UAS > median:")
    for i in range(len(nama_mahasiswa)):
        if nilai_array[i][2] > median:  # cek nilai UAS
            print(nama_mahasiswa[i])

# fungsi menampilkan 3 nilai tertinggi
def tiga_tertinggi():
    nilai_akhir = hitung_nilai_akhir()

    # argsort untuk mendapatkan indeks urutan nilai
    idx = np.argsort(nilai_akhir)[-3:][::-1]

    print("3 Nilai Tertinggi:")
    for i in idx:
        print(nama_mahasiswa[i], nilai_akhir[i])

# fungsi mencari mahasiswa
def cari_mahasiswa():
    nama = input("Masukkan nama: ")
    if nama in nama_mahasiswa:
        i = nama_mahasiswa.index(nama)
        print(nama, nilai_array[i])
    else:
        print("Tidak ditemukan")

# fungsi update nilai
def update_nilai():
    nama = input("Masukkan nama: ")
    if nama in nama_mahasiswa:
        i = nama_mahasiswa.index(nama)
        tugas = float(input("Tugas baru: "))
        uts = float(input("UTS baru: "))
        uas = float(input("UAS baru: "))
        nilai_array[i] = [tugas, uts, uas]  # update data
    else:
        print("Tidak ditemukan")

# fungsi hapus mahasiswa
def hapus_mahasiswa():
    global nilai_array
    nama = input("Masukkan nama: ")
    if nama in nama_mahasiswa:
        i = nama_mahasiswa.index(nama)
        nama_mahasiswa.pop(i)  # hapus nama
        nilai_array = np.delete(nilai_array, i, axis=0)  # hapus baris array
    else:
        print("Tidak ditemukan")

# menu utama
while True:
    print("\nMENU")
    print("1. Input Data")
    print("2. Tampilkan Array")
    print("3. Nilai Akhir")
    print("4. Analisis")
    print("5. 3 Tertinggi")
    print("6. Cari")
    print("7. Update Nilai")
    print("8. Hapus")
    print("9. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1": input_data()
    elif pilih == "2": tampilkan_array()
    elif pilih == "3": tampilkan_nilai_akhir()
    elif pilih == "4": analisis_kelas()
    elif pilih == "5": tiga_tertinggi()
    elif pilih == "6": cari_mahasiswa()
    elif pilih == "7": update_nilai()
    elif pilih == "8": hapus_mahasiswa()
    elif pilih == "9": break