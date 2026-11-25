# Bab 12: Enkapsulasi dalam Python

class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    def tampilkan_saldo(self):
        print("Pemilik:", self.pemilik)
        print("Saldo:", self.__saldo)

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print("Saldo berhasil ditambahkan.")
        else:
            print("Jumlah harus lebih dari 0.")

# Membuat objek
rekening1 = Rekening("Dandy", 100000)

# Memanggil method
rekening1.tampilkan_saldo()
rekening1.tambah_saldo(50000)
rekening1.tampilkan_saldo()