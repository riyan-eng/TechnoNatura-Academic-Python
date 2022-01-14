class Person():
    def __init__(self, name):
        self.name = name
    
    def say_hay(self):
        print('halo, nama saya adalah', self.name)

p = Person('Riyan')
p.say_hay()