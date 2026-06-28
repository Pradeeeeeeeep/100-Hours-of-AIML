class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def greet(self):
        print(f"Hello, my name is {self.name}")

Student1 = Student("John", 20, "A")
Student2 = Student("Alice", 22, "B")
Student1.greet()
Student2.greet()