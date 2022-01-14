from time import perf_counter


class Person():
    population = 0
    def __init__(self, name):
        self.name = name
        print("(memperkenalkan {})".format(self.name))
        Person.population += 1
    
    def die(self):
        print("{} telah dibunuh".format(self.name))
        Person.population -= 1
        if Person.population == 0:
            print("{} adalah yang terakhir".format(self.name))
        else:
            print("masih ada {:d} orang hidup".format(Person.population))

    def say_hay(self):
        print("halo, nama saya {}".format(self.name))
    
    @classmethod
    def how_many(cls):
        print("kita mempunyai {:d} orang".format(cls.population))

dani = Person("Dani")
dani.say_hay()
Person.how_many()