class Parent:
    def displayParent(self):
        print("This is the Parent class")


class Child(Parent):
    def displayChild(self):
        print("This is the Child class")
c = Child()
c.displayParent()
c.displayChild()