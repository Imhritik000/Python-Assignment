"""1. Write a Python program to convert kilometers to miles?
2. Write a Python program to convert Celsius to Fahrenheit?
3. Write a Python program to display calendar?
4. Write a Python program to solve quadratic equation?
5. Write a Python program to swap two variables without temp variable?"""


#1. Write a Python program to convert kilometers to miles?

kilometer = float(input("Enter the value of km to convert into miles : "))
mile = 1.609*kilometer
print(f"There are {mile} miles in {kilometer} kilometer  ")


#2. Write a Python program to convert Celsius to Fahrenheit?

Celsius = float(input("Enter the value of celsius to convert in to fahrenheit : "))
Fahrenheit = (Celsius*9/5 +32)
print(f"There are {Fahrenheit} Fahrenheit in {Celsius} Celsius")



#3. Write a Python program to display calendar?

import calendar
Year = int(input("Enter Year : "))
Month = int(input("Enter month : "))

Calendar = calendar.month( Year , Month )
print(Calendar)



#4. Write a Python program to solve quadratic equation?

import cmath
#complex math module

a = int(input("enter the value of a , a!=0 : "))
b = int(input("enter the value of b : "))
c = int(input("enter the value of c : "))

#Find the value of discriminant (d)
d = (b**2) - (4*a*c)

#find roots
Root1 = (- b - cmath.sqrt(d)) / (2*a)
Root2 = (- b + cmath.sqrt(d)) / (2*a)

print(f"the value of root 1 is {Root1} and value of root2 is {Root2}")



#5.Write a Python program to swap two variables without temp variable?

Variable1 = input("Enter your first variable here : ")
Variable2 = input("Enter your second variable here : ")

Varibale1,Variable2 = Variable2,Variable1
print("the value of First Variable after swap is " , Varibale1)
print("The value of Second Variable after swap is ", Variable2)