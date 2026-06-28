class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Alice")

print(student1.name)

student1.name = "Pradeep"

print(student1.name)