#Python Assignment 1

"""1. Write a Python program to print "Hello Python"?
2. Write a Python program to do arithmetical operations addition and division?
3. Write a Python program to find the area of a triangle?
4. Write a Python program to swap two variables?
5. Write a Python program to generate a random number?"""


#1. Write a Python program to print "Hello Python"?

print("Hello Python")




#2. Write a Python program to do arithmetical operations addition and division?

Expression = eval(input("Enter your question/arithmetical operation here : "))
print(Expression)



#3. Write a Python program to find the area of a triangle?

Base = float(input("Enter triangle base here : "))
Height = float(input("Enter triangle Height here : "))
Area_of_triangle = 0.5*Base*Height
print(Area_of_triangle)



#4. Write a Python program to swap two variables?

#Solution 1
A = int(input("enter the value of A :"))
B = int(input("enter the value of B :"))
A,B = B,A
print("the value of A after swapping is :", A)
print("the value of B after swapping is :", B)

#Solution 2
A = int(input("enter the value of A :"))
B = int(input("enter the value of B :"))
temp1 = A
A=B
B = temp1

print("the value of A after swapping is :", A)
print("the value of B after swapping is :", B)



#5. Write a Python program to generate a random number?

import random
print(random.randint(0,9))

