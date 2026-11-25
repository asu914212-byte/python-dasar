# Bab 17: Penanganan File dalam Python

# Menulis data ke file
with open("data_siswa.txt", "w") as file:
    file.write("Nama: Dandy\n")
    file.write("Kelas: XI RPL B\n")
    file.write("Jurusan: Rekayasa Perangkat Lunak\n")

print("Data berhasil disimpan.")

# Membaca isi file
with open("data_siswa.txt", "r") as file:
    isi = file.read()

print("\nIsi File:")
print(isi)