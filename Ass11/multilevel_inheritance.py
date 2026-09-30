class Grandparent:
    def showGrandparent(self):
        print("This is the Grandparent class")

class Parent(Grandparent):
    def showParent(self):
        print("This is the Parent class")

class Child(Parent):
    def showChild(self):
        print("This is the Child class")
c = Child()
c.showGrandparent()
c.showParent()
c.showChild()