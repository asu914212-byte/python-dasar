# Bab 10: Kamus (Dictionary) dalam Python

# Membuat dictionary
siswa = {
    "nama": "Dandy",
    "kelas": "XI RPL B",
    "umur": 17,
    "jurusan": "Rekayasa Perangkat Lunak"
}

# Menampilkan data
print("Data Siswa:")
print("Nama:", siswa["nama"])
print("Kelas:", siswa["kelas"])
print("Umur:", siswa["umur"])
print("Jurusan:", siswa["jurusan"])

# Menambahkan data
siswa["hobi"] = "Menggambar"

print("Hobi:", siswa["hobi"])

# Mengubah data
siswa["kelas"] = "XI RPL B"

print("Data Lengkap:", siswa)