import numpy as np

# Menentukan jumlah mahasiswa
n = int(input("Masukkan jumlah mahasiswa: "))

# Membuat list kosong
nama = []
nim = []
nilai = []
tahun = []

# Input data
for i in range(n):
    print("\nData mahasiswa ke-", i+1)
    nama.append(input("Nama: "))
    nim.append(input("NIM: "))
    nilai.append(float(input("Nilai: ")))
    tahun.append(int(input("Tahun Masuk: ")))

# Mengubah nilai menjadi array numpy
nilai_np = np.array(nilai)

# Menampilkan semua data
print("\n=== DATA MAHASISWA ===")
for i in range(n):
    print("\nData Mahasiswa",i+1,"\nNama:",nama[i],"\nNIM:",nim[i], "\nNilai:",nilai[i], "\nTahun Masuk:",tahun[i])

# Statistik nilai
print("\nNilai Tertinggi :", np.max(nilai_np))
print("Nilai Terendah :", np.min(nilai_np))
print("Nilai Rata-rata :", np.mean(nilai_np))

# Pencarian mahasiswa
cari = input("\nMasukkan Nama atau NIM yang dicari: ")

print("\n=== HASIL PENCARIAN ===")
for i in range(n):
    if cari == nama[i] or cari == nim[i]:
        print("Nama :", nama[i])
        print("NIM :", nim[i])
        print("Nilai :", nilai[i])
        print("Tahun Masuk :", tahun[i])
        