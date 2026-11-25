# Bab 7: Alur Kontrol dalam Python

# Percabangan if-else
nilai = 85

if nilai >= 75:
    print("Keterangan: Lulus")
else:
    print("Keterangan: Tidak Lulus")

# Percabangan if-elif-else
nilai = 85

if nilai >= 90:
    print("Predikat: A")
elif nilai >= 80:
    print("Predikat: B")
elif nilai >= 70:
    print("Predikat: C")
else:
    print("Predikat: D")

# Perulangan for
print("Perulangan For:")
for angka in range(1, 6):
    print(angka)

# Perulangan while
print("Perulangan While:")
hitung = 1

while hitung <= 5:
    print(hitung)
    hitung += 1