import numpy as np

# jumlah barang
n = int(input("Masukkan jumlah barang: "))

nama = []
kode = []
jumlah = []
harga = []

for i in range(n):
    print("\nData barang ke-", i+1)
    nama.append(input("Nama Barang: "))
    kode.append(input("Kode Barang: "))
    jumlah.append(int(input("Jumlah: ")))
    harga.append(float(input("Harga per Unit: ")))

# Mengubah ke numpy array
jumlah_np = np.array(jumlah)
harga_np = np.array(harga)

# menghitung total nilai inventaris
total = jumlah_np * harga_np

print("\n=== DATA INVENTARIS ===")
for i in range(n):
    print("\nNama Barang:",nama[i],"\nKode Barang:", kode[i],"\nJumlah Barang:", jumlah[i],"\nHarga Barang:", harga[i], "\nTotal Nilai:", total[i])

# Pencarian barang
cari = input("\nMasukkan Nama atau Kode Barang yang dicari: ")

print("\n=== HASIL PENCARIAN ===")
for i in range(n):
    if cari == nama[i] or cari == kode[i]:
        print("Nama Barang :", nama[i])
        print("Kode Barang :", kode[i])
        print("Jumlah :", jumlah[i])
        print("Harga per Unit :", harga[i])
        print("Total Nilai :", total[i])