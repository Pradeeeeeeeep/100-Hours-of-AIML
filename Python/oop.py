class Student:
    def __init__(self, name, age=21):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")
        print(f"And I am {self.age} years old.")

Student1 = Student("John", 24)
Student2 = Student("Alice")
Student1.greet()
Student2.greet()