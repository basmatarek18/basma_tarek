class grandParent():
    def __init__(self, name):
        self.name=name
    def showName(self):
        return self.name

class Parent(grandParent):
    def __init__(self, name, address):
        self.address = address
        grandParent.__init(self,name)       

    def showAddress(self):
        return self.address

class Child(grandParent, Parent):
    def __init__(self,name,address, age):
        self.age=age
        grandParent.__init__(self,name)
        Parent.__init__(self,address)
    def showAge(self):
        return self.age

grand1=grandParent("Ali")                
parent1=Parent("Tarek", "Tanta")
child1=Child("Basma","Tanta",19)
grand1.showName()
parent1.showAddress()
child1.showAge()