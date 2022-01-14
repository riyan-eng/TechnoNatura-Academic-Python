x = 50

def func(x):
    print('x adalah', x)
    x = 2
    print('ganti local x dengan', x)

func(x)
print('x tetap', x)