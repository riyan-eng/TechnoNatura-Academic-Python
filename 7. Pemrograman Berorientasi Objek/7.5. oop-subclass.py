from select import select


class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell(self):
        print("nama: {}, umur: {}".format(self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
    def tell(self):
        SchoolMember.tell(self)
        print("salary: {}".format(self.salary))

class Student(Teacher):
    def __init__(self, name, age, salary, student):
        Teacher.__init__(self, name, age, salary)
        self.student = student
    def tell(self):
        Teacher.tell(self)
        print("murid: {}".format(self.student))

# rahma = Teacher("rahma", "21 tahun", "Rp 3.000.000")
# rahma.tell()

angga = Student("rahma", "21 tahun", "Rp 3.000.000", "angga")
angga.tell()