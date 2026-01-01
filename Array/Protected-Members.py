class Student:
    def __init__(self,marks):
        self._marks =marks

class Result(Student):
    def show(self):
        print(self._marks)
r = Result(80)
r.show()