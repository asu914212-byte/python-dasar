# Bab 15: Abstraksi dalam Python

from abc import ABC, abstractmethod

# Class abstrak
class Kendaraan(ABC):
    @abstractmethod
    def bergerak(self):
        pass

# Class turunan
class Mobil(Kendaraan):
    def bergerak(self):
        print("Mobil bergerak menggunakan roda.")

class Pesawat(Kendaraan):
    def bergerak(self):
        print("Pesawat bergerak menggunakan mesin.")

# Membuat objek
mobil = Mobil()
pesawat = Pesawat()

# Memanggil method
mobil.bergerak()
pesawat.bergerak()