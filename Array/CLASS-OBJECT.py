class Student:
    def __init__(self,name,age):
        self.name = name    # Data
        self.age = age      # Data
    def display(self):      # Behavior 
        print("Name:-",self.name)
        print("Age:-",self.age)
    def result(self):       # Behavior 
        if self.age >= 40:
            print("Available")    # Data + Behavior = Object
        else:
            print("Not Available")
#Object Creation
s1 = Student("Raghav",30)
#Access Behavior
s1.display()
s1.result()