#python calculater 
a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
operator = input("enter the operator:")
if operator == '+':
    print("the addition of a+b:",a+b)
elif operator == '-':
    print("the subtraction of a-b:",a-b)
elif operator == '*':
    print("the multiplication of a*b:",a*b)
elif operator == '/':
    print("the division of a/b:",a/b)
elif operator == '%':
    print("the modulus of a%b:",a%b)
else:
    print("invalid operator:")


#basic arithmetic_operator calculator 

num1 = float(input("enter the no 1: "))
num2 = float(input("enter the no 2: "))
operator = input("enter the operator: ")

if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
elif operator=='%':
    print(num1%num2)
else:
    print("invalid number: ")
