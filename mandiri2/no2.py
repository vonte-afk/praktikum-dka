import numpy as np  # untuk array numerik
import random  # untuk angka acak

# list untuk menyimpan data
nama = []
kode = []
data_numerik = []

# input jumlah pelanggan
n = int(input("Jumlah pelanggan: "))

for i in range(n):
    print(f"\nData pelanggan ke-{i+1}")
    nama_p = input("Nama: ")
    belanja = int(input("Total Belanja: "))
    transaksi = int(input("Jumlah Transaksi: "))

    # membuat kode undian acak
    kode_undian = f"UND-{random.randint(1000,9999)}"

    # simpan data
    nama.append(nama_p)
    kode.append(kode_undian)
    data_numerik.append([belanja, transaksi])

# ubah ke numpy array
data_numerik = np.array(data_numerik)

# tampilkan data
print("\nDATA PELANGGAN")
for i in range(n):
    print(nama[i], kode[i], data_numerik[i])

# hitung rata-rata total belanja
rata = np.mean(data_numerik[:,0])
print("Rata-rata belanja:", rata)

# tentukan pelanggan prioritas (belanja > rata-rata)
prioritas = data_numerik[:,0] > rata

# tentukan peserta undian (transaksi >= 3)
peserta = data_numerik[:,1] >= 3

# menentukan slot undian
slot = []
for i in range(n):
    belanja = data_numerik[i][0]
    s = 0

    # aturan slot berdasarkan belanja
    if belanja < 300000:
        s = 1
    elif belanja <= 700000:
        s = 2
    else:
        s = 3

    # tambahan slot jika prioritas
    if prioritas[i]:
        s += 2

    slot.append(s)

# membuat daftar tiket undian
tiket = []
for i in range(n):
    if peserta[i]:  # hanya peserta yang memenuhi syarat
        tiket += [i] * slot[i]  # semakin besar slot, semakin banyak peluang

# proses undian
pemenang = set()
while len(pemenang) < 2 and tiket:
    pilih = random.choice(tiket)  # pilih secara acak
    pemenang.add(pilih)  # set agar tidak duplikat

# tampilkan pemenang
print("\nPEMENANG:")
for i in pemenang:
    print(nama[i], kode[i])

# fitur pencarian berdasarkan kode
cari = input("\nMasukkan kode undian: ")
if cari in kode:
    i = kode.index(cari)
    print("Ditemukan:", nama[i], data_numerik[i])
else:
    print("Tidak ditemukan")