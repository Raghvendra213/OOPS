class Student:
    def __init__(self,marks):
        self.marks =marks

class Result(Student):
    def show(self):
        print(self.marks)
r = Result(80)
r.show()