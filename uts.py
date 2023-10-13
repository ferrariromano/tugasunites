#Program Asli 
print('=' * 25)
print('Operasi Matematika')
print(' 1. Jumlah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. Kali \t [*]')
print(' 4. Bagi \t [/]')
print('=' * 25)
operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))
print('=' * 25)
if operasi == '1':
    hasil = bilangan_1 + bilangan_2
    print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
    hasil = bilangan_1 - bilangan_2
    print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
    hasil = bilangan_1 * bilangan_2
    print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
    hasil = bilangan_1 / bilangan_2
    print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
    print('Tidak valid')

#Program Unitest
# import unittest
# def operasi_matematika(operasi, bilangan_1, bilangan_2):
#     if operasi == '1':
#         hasil = bilangan_1 + bilangan_2
#         return f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}'
#     elif operasi == '2':
#         hasil = bilangan_1 - bilangan_2
#         return f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}'
#     elif operasi == '3':
#         hasil = bilangan_1 * bilangan_2
#         return f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}'
#     elif operasi == '4':
#         if bilangan_2 == 0:
#             return 'Tidak bisa membagi dengan nol.'
#         hasil = bilangan_1 / bilangan_2
#         return f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}'
#     else:
#         return 'Operasi tidak valid'

# class TestOperasiMatematika(unittest.TestCase):
#     def test_penjumlahan(self):
#         self.assertEqual(operasi_matematika('1', 3, 2), 'Hasil operasi dari 3 + 2 = 5')
#         print(operasi_matematika('1', 3, 2))

#     def test_pengurangan(self):
#         self.assertEqual(operasi_matematika('2', 8, 4), 'Hasil operasi dari 8 - 4 = 4')
#         print(operasi_matematika('2', 8, 4))

#     def test_perkalian(self):
#         self.assertEqual(operasi_matematika('3', 5, 6), 'Hasil operasi dari 5 * 6 = 30')
#         print(operasi_matematika('3', 5, 6))

#     def test_pembagian(self):
#         self.assertEqual(operasi_matematika('4', 10, 2), 'Hasil operasi dari 10 / 2 = 5')
#         self.assertEqual(operasi_matematika('4', 5, 0), 'Tidak bisa membagi dengan nol.')
#         print(operasi_matematika('4', 10, 2))
#         print(operasi_matematika('4', 5, 0))

#     def test_operasi_tidak_valid(self):
#         self.assertEqual(operasi_matematika('5', 2, 3), 'Operasi tidak valid')
#         print(operasi_matematika('5', 2, 3))

# if __name__ == '__main__':
#     unittest.main()
