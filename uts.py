# def tambah(a, b):
#     return a + b

# def kurang(a, b):
#     return a - b

# def kali(a, b):
#     return a * b

# def bagi(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Pembagian oleh nol tidak diizinkan"

# def pangkat(a, b):
#     return a ** b

# # Contoh penggunaan fungsi
# print("Hasil Penambahan: ", tambah(2, 3))
# print("Hasil Pengurangan: ", kurang(5, 3))
# print("Hasil Perkalian: ", kali(2, 3))
# print("Hasil Pembagian: ", bagi(6, 2))
# print("Hasil Pemangkatan: ", pangkat(2, 3))

#unitest 
import unittest

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Pembagian oleh nol tidak diizinkan"

def pangkat(a, b):
    return a ** b

class TestKalkulator(unittest.TestCase):
    # Metode pengujian untuk fungsi tambah
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
        self.assertEqual(tambah(-2, 3), 1)

    # Metode pengujian untuk fungsi kurang
    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)
        self.assertEqual(kurang(3, 5), -2)

    # Metode pengujian untuk fungsi kali
    def test_kali(self):
        self.assertEqual(kali(2, 3), 6)
        self.assertEqual(kali(-2, 3), -6)

    # Metode pengujian untuk fungsi bagi
    def test_bagi(self):
        self.assertEqual(bagi(6, 2), 3)
        self.assertEqual(bagi(5, 0), "Pembagian oleh nol tidak diizinkan")

    # Metode pengujian untuk fungsi pangkat
    def test_pangkat(self):
        self.assertEqual(pangkat(2, 3), 8)
        self.assertEqual(pangkat(3, 2), 9)

if __name__ == '__main__':
    unittest.main()