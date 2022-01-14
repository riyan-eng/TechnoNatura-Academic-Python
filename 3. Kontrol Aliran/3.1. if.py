nomor = 23
tebakan = int(input('masukkan sebuah angka: '))

if tebakan == nomor:
    print('selamat, tebakan kamu benar')
    print('(tetapi kamu tidak mendapatkan hadiah apapun)')
elif tebakan < nomor:
    print('tidak, nomornya lebih besar dari itu')
else:
    print('tidak, nomornya lebih kecil dari itu')
print('selesai')