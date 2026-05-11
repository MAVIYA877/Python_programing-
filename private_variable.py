#A private variable is a variable inside a class that cannot be accessed from outside the class.
class variable :
    def __init__(self):
        self.__a = 10
        self.__b = 20
        self.__c = 30

    def show(self):
        print("a:",self.__a)
        print("b:",self.__b)
        print("c:",self.__c)
        print("aadtion of a+b+c =",self.__a+self.__b+self.__c)

s1 = variable()
s1.show()