# Bab 11: Kelas dan Objek dalam Python

# Membuat class
class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)

# Membuat objek
siswa1 = Siswa("Dandy", "XI RPL B")

# Memanggil method
siswa1.perkenalan()