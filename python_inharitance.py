#Inheritance in Python is a core principle of object-oriented programming (OOP) that allows a new class (child class or subclass) to inherit attributes and methods from an existing class (parent class or superclass).
#sinlge inharitance
class car:
    def speed(slef):
        print("speed:",200)

class bike(car):
    def ride(self):
        print("riding is bike")

b1 = bike()
b1.speed()
b1.ride()

#multiple inheritance 
class father:
    def news(self):
        print("newspaper.")
    
class mother:
    def cook(self):
        print("cooking.")

class son(father,mother):
    def code(self):
        print("coding")

c1 = son()
c1.news()
c1.cook()
c1.code()

#multilevel inheritance 
class a:
    def showa(self):
        print("this is class a:")

class b(a):
    def showb(self):
        print("thid is class c:")

class c(b):
    def showc(self):
        print("this is class c:")

s1 = c()
s1.showa()
s1.showb()
s1.showc() 

#hierarchical inheritance 
class parents:
    def showparents(self):
        print("this is parents class.")

class child1(parents):
    def showchild1(self):
        print("this is child1 class.")

class child2(parents):
    def showchild2(self):
        print("this is child2 class.")

class child3(parents):
    def showchild3(self):
        print('this is child3 class.')

c1 = child1()
c2 = child2()
c3 = child3()

c1.showparents()
c1.showchild1()

c2.showparents()
c2.showchild2()

c3.showparents()
c3.showchild3()

#hybrid inheritance 
class a:
    def show1(self):
        print("this is class a.")

class b(a):
    def show2(self):
        print("this is class b.")

class c:
    def show3(self):
        print("this is class c.")

class d(b,c):
    def show4(self):
        print("this is class d.")

s1 = d()
s1.show1()
s1.show2()
s1.show3()
s1.show4()
