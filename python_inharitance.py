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
#inheritance prectice
 
#single inheritance 
class a:
    def show1(slef):
        print("this is class a.")

class b(a):
    def shiw2():
        print("this is class b.")
s1 = b()
s1.show1()
s1.show1()

#multiple inheritance
class a:
    def display1(self):
        print("strong a.")

class b():
    def display2(self):
        print("strong b.")

class c(a,b):
    def display3(self):
        print("strong c")

d1 = c()
d1.display1()
d1.display2()
d1.display3()

#multilevel inheritance 
class a:
    def sayar1(self):
        print("sayar 1:")

class b(a):
    def sayar2(self):
        print("sayar 2:")

class c(b):
    def sayar3(self):
        print("sayar 3:")

s1 = c()
s1.sayar1()
s1.sayar2()
s1.sayar3()

#hierarchical inheritance 
class parents:
    def ride(self):
        print("riding car.")

class child1(parents):
    def code(self):
        print("coding.")

class child2(parents):
    def game(self):
        print("gaming.")
class child3(parents):
    def strong(self):
        print("strong boy 3.")

s1 = child1()
s2 = child2()
s3 = child3()

s1.ride()
s1.code()

s2.ride()
s2.game()

s3.ride()
s3.strong()
 
#hybrid inheritance 
class a:
    def display1(self):
        print("display 1:")
class b(a):
    def display2(self):
        print("display 2:")
class c:
    def display3(self):
        print("display 3:")
class d(b,c):
    def display4(self):
        print("display 4:")

d1 = d()
d1.display1()
d1.display2()
d1.display3()
d1.display4()

#inharitance prectice

#single inheritance 
class parents:
    def news(self):
        print("read a newspaper")

class child(parents):
    def code(self):
        print("coding")
a1 = child()
a1.code()
a1.news()

#multiple inheritance 
class a:
    def display1(self):
        print("hello1")
class b:
    def display2(self):
        print("hello2")
class c(a,b):
    def display3(self):
        print("hello3")

a1 = c()
a1.display1()
a1.display2()
a1.display3() 

#multilevel inheritance 
class a:
    def show1(self):
        print("show1:")

class b(a):
    def show2(self):
        print("show2:")

class c(b):
    def show3(self):
        print("show3:")

a1 = c()
a1.show1()
a1.show2()
a1.show3()

#hierarchical inheritance 
class parents:
    def drive(self):
        print("drive car:")

class child1(parents):
    def code(self):
        print("coding:")

class child2(parents):
    def play(self):
        print("playing:")
class child3(parents):
    def display(self):
        print("this is child3:")

a1 = child1()
a2 = child2()
a3 = child3()

a1.code()
a1.drive()
a3.display()

#hybrid inheritance 
class a:
    def display1(self):
        print("hello 1:")

class b(a):
    def display2(self):
        print("hello 2:")

class c:
    def display3(self):
        print("hello 3:")

class d(b,c):
    def display4(self):
        print("hello 4:")

a1 = d()
a1.display1()
a1.display2()
a1.display3()
a1.display4()