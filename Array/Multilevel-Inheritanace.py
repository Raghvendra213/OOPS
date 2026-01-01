class Grandfather:
    def land(self):
        print("Grandfather")
class Father(Grandfather):
    def house(self):
        print("Father")
class Son(Father):
    def bike(self):
        print("Son Bike")
s1 =Son()
s1.land()   #GrandFather Method
s1.house()  #Father Method
s1.bike()   #Son Method