try:
    text = input('masukkan sesuatu -->')
except EOFError:
    print('kenapa kamu melakukan EOF?')
except KeyboardInterrupt:
    print('kenapa kamu membatalkan operasi')
else:
    print('kamu memasukkan {}'.format(text))