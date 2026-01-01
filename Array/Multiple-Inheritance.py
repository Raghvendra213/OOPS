class Father:
    def skills(self):
        print("Father Skills")
class Mother:
    def skills(self):
        print("Mother Skills.")
class Son(Father,Mother):  # Multilevel skills
    pass
S1 = Son()
S1.skills()