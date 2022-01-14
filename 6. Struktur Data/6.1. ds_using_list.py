shoplist = ['apel', 'mangga', 'wortel', 'pisang']
print('saya punya', len(shoplist), 'barang untuk dibeli')
print('barang itu adalah: ', end=' ')

for barang in shoplist:
    print(barang, end=' ')

print('\n saya juga membeli nasi')
shoplist.append('nasi')
print('daftar belanja saya sekarang adalah', shoplist)

print('saya akan mengurutkan daftar belanja sekarang')
shoplist.sort()
print('urutannya adalah', shoplist)

print('barang pertama yang akan saya beli adalah', shoplist[4])

barang_lama = shoplist[0]
del shoplist[0]

print('saya telah membeli', barang_lama)
print('daftar belanja saya sekarang adalah', shoplist)