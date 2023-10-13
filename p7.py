#Program Asli 
# def nilai_maksimal(deret_bilangan):
#     nilai_terbesar = deret_bilangan[0]
    
#     for nilai in deret_bilangan:
#         if nilai > nilai_terbesar:
#             nilai_terbesar = nilai
#     return nilai_terbesar

# def nilai_minimal(deret_bilangan):
#     nilai_terkecil = deret_bilangan[0]
#     for nilai in deret_bilangan:
#         if nilai < nilai_terkecil:
#             nilai_terkecil = nilai
#     return nilai_terkecil

# a = [3, 20, 100, -35, 50]
# print(a)
# print('Nilai terbesar:', nilai_maksimal(a))
# print('Nilai terkecil:', nilai_minimal(a))

#Program Unitest
import unittest

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]
    
    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai
    return nilai_terkecil

# Menampilkan nilai terbesar dan terkecil sebelum pengujian
a = [3, 20, 100, -35, 50]
print('Deret Bilangan:', a)
print('Nilai terbesar:', nilai_maksimal(a))
print('Nilai terkecil:', nilai_minimal(a))

class TestNilaiMaksimalMinimal(unittest.TestCase):
    def test_nilai_maksimal(self):
        self.assertEqual(nilai_maksimal([3, 20, 100, -35, 50]), 100)
        self.assertEqual(nilai_maksimal([-5, -10, -20, -1, -2]), -1)
        self.assertEqual(nilai_maksimal([0]), 0)

    def test_nilai_minimal(self):
        self.assertEqual(nilai_minimal([3, 20, 100, -35, 50]), -35)
        self.assertEqual(nilai_minimal([-5, -10, -20, -1, -2]), -20)
        self.assertEqual(nilai_minimal([0]), 0)

if __name__ == '__main__':
    unittest.main()