# Bab 8: Fungsi dalam Python

# Membuat fungsi sederhana
def salam():
    print("Halo, selamat belajar Python!")

# Fungsi dengan parameter
def sapa(nama):
    print("Selamat datang,", nama)

# Fungsi dengan nilai kembali
def tambah(a, b):
    return a + b

# Memanggil fungsi
salam()
sapa("Dandy")

hasil = tambah(10, 5)
print("Hasil penjumlahan:", hasil)