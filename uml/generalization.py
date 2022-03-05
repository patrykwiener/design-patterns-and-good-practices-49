class Person:
    def __init__(self, name):
        self._name = name


class Student(Person):

    def __init__(self, name, university):
        super().__init__(name)
        self.university = university


class Programmer(Person):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company


class StudentProgrammer(Student, Programmer):
    def __init__(self, name, university, company):
        Student.__init__(self, name=name, university=university)
        Programmer.__init__(self, name=name, company=company)


if __name__ == '__main__':
    student = Student('Flip', 'Politechnika Wroclawska')
    programmer = Programmer('Flap', 'Software Development Academy')
    student_programmer = StudentProgrammer('Patryk', 'POLSL', 'RA')
    print(student_programmer._name)
    print(student_programmer.company)
    print(student_programmer.university)
