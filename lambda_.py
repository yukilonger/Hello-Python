class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = []
students.append(Student('whl', 36))
students.append(Student('lzj', 37))
students.append(Student('xxx', 35))
students.append(Student('yyy', 38))

z = min(students, key=lambda x:x.age)
print(z.name)