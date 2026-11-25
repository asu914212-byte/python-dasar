# Bab 16: Penanganan Pengecualian Python

try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2

    print("Hasil pembagian:", hasil)

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Angka tidak boleh dibagi dengan nol!")

finally:
    print("Program selesai.")