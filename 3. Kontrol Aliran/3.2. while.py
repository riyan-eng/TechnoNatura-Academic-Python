nomor = 23
berjalan = True


while berjalan:
    tebakan = int(input('masukkan sebuah angka: '))
    if tebakan == nomor:
        print('selamat, kamu berhasil menebaknya')
        berjalan = False
    elif tebakan < nomor:
        print('tidak, nomornya lebih besar dari itu')
    else:
        print('tidak, nomornya lebih kecil dari itu')
else:
    print('while loop telah berakhir')
print('selesai')