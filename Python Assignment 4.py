"""1. Write a Python Program to Find the Factorial of a Number?
2. Write a Python Program to Display the multiplication Table?
3. Write a Python Program to Print the Fibonacci sequence?
4. Write a Python Program to Check Armstrong Number?
5. Write a Python Program to Find Armstrong Number in an Interval?
6. Write a Python Program to Find the Sum of Natural Numbers?"""


#1. Write a Python Program to Find the Factorial of a Number?

Num = int(input("enter the number here to find it's factorial :"))
factorial = 1

if Num < 0 :
    print("factorial of negative number do not exist")

elif Num == 0 :
    print("the factorial of 0 is 1 ")

else :
    for i in range(1, Num + 1):
        factorial = factorial * i
    print("The factorial of", Num, "is", factorial)







#2. Write a Python Program to Display the multiplication Table?

Num = int(input("Enter the number of which table you want : "))

for i in range (1,11):
    print(Num,"*", i ,"=",Num*i)



#3. Write a Python Program to Print the Fibonacci sequence?

a = 0
b = 1

Num = int(input("enter the num here : "))

if Num < 0 :
    print ("Please enter positive number")

elif Num == 1:
    print("0")

else :
    print(a)
    print(b)

    for i in range(1,Num+1) :
        c = a+b
        a = b
        b = c
        print(c)



#4. Write a Python Program to Check Armstrong Number?

Num = int(input("enter the number here : "))
order = len(str(Num))
sum = 0
temp = Num

while temp>0:
    digit = temp%10
    power = digit**order
    sum = sum + power
    temp //= 10

if sum == Num :
    print("yes it is a Armstrong number")

else :
    print("No it is not a Armstrong number")



#5. Write a Python Program to Find Armstrong Number in an Interval?

Upper_limit = int(input("Enter the Upper limit here "))
Lower_limit = int(input("Enter the Lower limit here"))

for Num in range(Lower_limit,Upper_limit+1):
    Order = len(str(Num))
    sum = 0
    temp = Num
    while temp > 0:
        digit = temp % 10
        sum += digit** Order
        temp //= 10
        if Num == sum:
          print(Num)




#6. Write a Python Program to Find the Sum of Natural Numbers?
Num = int(input("enter the number here : "))

if Num < 0 :
    print("Please enter positive number ")

else :

    Sum = 0
    while Num > 0:
       Sum += Num
       Num -= 1

    print(Sum)