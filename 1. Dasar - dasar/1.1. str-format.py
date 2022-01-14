umur = 20
nama = 'Ahmad'

print('{0} berumur {1} tahun ketika menulis buku ini'.format(nama, umur))
print('kenapa {0} bermain dengan python?'.format(nama))

print('{} berumur {} tahun ketika menulis buku ini'.format(nama, umur))
print('kenapa {} bermain dengan python?'.format(nama))

print('{nama} berumur {umur} tahun ketika menulis buku ini'.format(nama=nama, umur=umur))
print('kenapa {nama} bermain dengan python?'.format(nama=nama))

print(f'{nama} berumur {umur} tahun ketika menulis buku ini')
print(f'kenapa {nama} bermain dengan python?')

print('a', end=' ')
print('b', end=' ')
print('c')