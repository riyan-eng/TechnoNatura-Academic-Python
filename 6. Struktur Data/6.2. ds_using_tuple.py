hewan = ('singa', 'gajah', 'pinguin')
print('jumlah hewan yang ada di kebun binatang adalah', len(hewan))

hewan_baru = 'monyet', 'onta', hewan
print('jumlah kandang yang ada di kebun binatang baru adalah', len(hewan_baru))
print('semua hewan yang ada di kebun binatang adalah', hewan_baru)
print('binatang dari kebun binatang yang lama adalah', hewan)
print('binatang terakhir yang dibawa dari kebun binatang yang lama adalah', hewan_baru[2][2])
print('jumlah hewan yang berada di kebun binatang yang baru adalah', len(hewan_baru)-1+len(hewan_baru[2]))