class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

s1 = Student("Maha", 19, "CSE")
s2 = Student("Anu", 20, "CSE")

s1.display()
s2.display()