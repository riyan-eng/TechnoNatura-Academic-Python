def total(a=5, *numbers, **phonebook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

total(10, 1,2,3, Jack=111,John=222,Inge=333)