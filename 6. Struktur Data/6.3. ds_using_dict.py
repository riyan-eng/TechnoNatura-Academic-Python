ab = 'address book'
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print('alamat Swaroop adalah', ab['Swaroop'])

del ab['Spammer']

print('\n ada {} kontak di buku alamat \n'.format(len(ab)))

for nama, alamat in ab.items():
    print('kontak {} di {}'.format(nama, alamat))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('alamat Guido di', ab['Guido'])