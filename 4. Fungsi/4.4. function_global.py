x = 50

def func():
    global x
    print('x adalah', x)
    x = 2
    print('ganti global x dengan', x)

func()
print('nilai x tetap', x)