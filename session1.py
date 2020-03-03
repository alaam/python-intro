class Person:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def printName(self):
        print self.name


class Student(Person):
    def __init__(self, name, grade, age, address, grades):
        self.name = name
        self.grade = grade
        self.age = age
        self.address = address
        self.grades = grades

    def maxGrade(self):
        print max(self.grades)

    def whatAmI(self):
        print "student"

    def getAverage(self):
        print self.name

        # integer, string, list, dictionary

        sum = 0
        for grade in self.grades:
            sum = sum + grade

        average = sum / len(self.grades)
        print average


class Teacher(Person):
    def whatAmI(self):
        print "teacher"


class Principal(Person):
    def whatAmI(self):
        print "principal"


abdullah = Person("Abdullah", 15, "345 state st", "something@someothng.com")
abdullah.printName()

alaa = Teacher("Alaa", 12, "123 main st", "alaa.mahmoud@somedomain.com")
aisha = Student("Aisha", 1, 13, "123 main st", [10, 15, 35, 40])
mouad = Student("Mouad", 1, 12, "123 main st", [12, 25, 40, 35])

alaa.printName()
alaa.whatAmI()

aisha.printName()
aisha.getAverage()
aisha.whatAmI()

aisha.maxGrade()

mouad.printName()
mouad.getAverage()
mouad.maxGrade()
