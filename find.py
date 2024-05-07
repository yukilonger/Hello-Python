class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = []
students.append(Student('whl', 36))
students.append(Student('lzj', 37))
students.append(Student('xxx', 35))
students.append(Student('yyy', 38))

a = list(filter(lambda x:x.name=='whl', students))
print(a[0].age)


a = 'SH.600600'
c = '600600'
b = a.find('.')
d = c.find('.')
print('find . 的索引：',d)