class Student:
    def setData(self):
        self.name = "Rengoku"
        self.age = 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1 = Student()
s1.setData()
s1.display()