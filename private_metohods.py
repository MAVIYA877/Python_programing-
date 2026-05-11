#A private method is a method (function inside a class) that you can only call inside the class, not outside.
class methods:

    def __init__(self,name,age,roll_no,address):
        self.name = name 
        self.age = age 
        self.roll_no = roll_no
        self.address = address

    def __private_methods(self):
        print("name:",self.name)
        print("age:",self.age)
        print("roll_no:",self.roll_no)
        print("address:",self.address)

    def public_methods(self):
        print("this is public methods.")
        self.__private_methods()

m1 = methods("mr.samad",18,1,"bengaluru")
m1.public_methods()