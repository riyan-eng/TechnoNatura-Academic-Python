while True:
    s = input('masukkan sesuatu: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('terlalu pendek')
        continue
    print('masukan telah cukup panjang')