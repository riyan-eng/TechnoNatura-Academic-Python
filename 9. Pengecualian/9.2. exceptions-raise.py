class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('masukkan sesuatu --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('kenapa kamu melakukan EOF?')
except ShortInputException as ex:
    print(('ShortInputException: isi masukan adalah ' + 'panjangnya {}, dan dikitnya {}').format(ex.length, ex.atleast))
else:
    print('tidak ada exceptions yang ditampilkan')