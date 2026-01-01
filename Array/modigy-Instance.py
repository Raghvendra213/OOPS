class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Rahul", 70)
s2 = Student("Neha", 90)

s1.marks = 85   # modify property

print(s1.marks)  # 85
print(s2.marks)  # 90
