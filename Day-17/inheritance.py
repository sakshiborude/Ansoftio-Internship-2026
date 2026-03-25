class Person:
 def __init__(self, name, age):
 self.name = name
 self.age = age
class Student(Person):
 def __init__(self, name, age, course):
 super().__init__(name, age)
 self.course = course
 def display(self):
 print("Name:", self.name)
 print("Age:", self.age)
 print("Course:", self.course)
s1 = Student("Anand", 23, "MCA")
s1.display()
