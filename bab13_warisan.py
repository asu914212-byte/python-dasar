# Bab 13: Warisan (Inheritance) dalam Python

# Class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print(self.nama, "mengeluarkan suara.")

# Class turunan
class Kucing(Hewan):
    def suara(self):
        print(self.nama, "berbunyi Meong!")

# Membuat objek
hewan1 = Hewan("Hewan")
kucing1 = Kucing("Milo")

# Memanggil method
hewan1.suara()
kucing1.suara()