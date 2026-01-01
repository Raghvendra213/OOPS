class Student:
    def __init__(self, name):
        self.name = name    # object data

    def show(self):
        print("Name:", self.name)

s1 = Student("Rahul")
s1.show()
