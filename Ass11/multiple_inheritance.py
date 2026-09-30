class Father:
    def showFather(self):
        print("This is the Father class")

class Mother:
    def showMother(self):
        print("This is the Mother class")

class Child(Father, Mother):
    def showChild(self):
        print("This is the Child class")
c = Child()
c.showFather()
c.showMother()
c.showChild()