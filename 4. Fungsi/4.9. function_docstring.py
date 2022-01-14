def maximum(x, y):
    '''
    print max dari dua angka.
    '''

    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else: 
        print(y, 'is maximum')

maximum(2,3)
print(maximum.__doc__)