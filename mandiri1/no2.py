# Fungsi untuk mengembalikan nilai Fibonacci ke-n
def fibonacci(n):
    # Dua nilai awal Fibonacci
    a = 0
    b = 1
    # Jika n = 1 maka hasilnya 0
    if n == 1:
        return a
    # Jika n = 2 maka hasilnya 1
    if n == 2:
        return b
    # Perulangan untuk menghitung Fibonacci ke-n
    for i in range(3, n + 1):
        c = a + b      # Menjumlahkan dua angka sebelumnya
        a = b          # Memindahkan nilai
        b = c
    return b          # Mengembalikan nilai Fibonacci ke-n

# Prosedur untuk mencetak barisan Fibonacci dari suku 1 sampai n
def cetakFibonacci(n):
    # Dua nilai awal Fibonacci
    a = 0
    b = 1
    # Perulangan mencetak sampai suku ke-n
    for i in range(1, n + 1):
        print(a, end=" ")   # Menampilkan angka Fibonacci
        c = a + b           # Menghitung angka berikutnya
        a = b               # Menggeser nilai
        b = c

# Input dari user
n = int(input("Masukkan jumlah suku Fibonacci: "))
# Memanggil fungsi untuk mendapatkan Fibonacci ke-n
hasil = fibonacci(n)
# Menampilkan hasil Fibonacci ke-n
print("Fibonacci ke-", n, "adalah:", hasil)
# Menampilkan barisan Fibonacci sampai suku ke-n
print("Barisan Fibonacci:")
cetakFibonacci(n)