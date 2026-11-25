# Bab 14: Polimorfisme dalam Python

class Kucing:
    def suara(self):
        print("Kucing berbunyi Meong!")

class Anjing:
    def suara(self):
        print("Anjing berbunyi Guk Guk!")

class Ayam:
    def suara(self):
        print("Ayam berbunyi Kukuruyuk!")

# Membuat objek
hewan = [Kucing(), Anjing(), Ayam()]

# Memanggil method yang sama
for item in hewan:
    item.suara()