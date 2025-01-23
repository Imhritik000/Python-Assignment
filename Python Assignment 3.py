"""1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
2. Write a Python Program to Check if a Number is Odd or Even?
3. Write a Python Program to Check Leap Year?
4. Write a Python Program to Check Prime Number?
5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?"""


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

Num = int(input("Enter your number here : "))
if Num < 0:
    print("Number is negative");
elif Num == 0:
    print ("Number is zero");
else:
    print("Number is positive")



#2. Write a Python Program to Check if a Number is Odd or Even?

Num = int(input("Enter your number here : "))
if Num % 2 == 0:
    print ("Number is even ")
#  % is modulo operator(to find the remainder of division of two number)
else :
    print("Number is odd")




#3. Write a Python Program to Check Leap Year?

Year = int(input("Enter year here :"))
if Year % 400 ==0 and Year % 100 == 0 :
    print(Year,"Is a leap year ")

elif Year % 4 == 0 and Year % 100 !=0 :
     print(Year,"Is a leap year")

else :
    print(Year,"Not a leap year")




#4. Write a Python Program to Check Prime Number?

Number = int(input("Enter number here :"))

if Number > 1:
    for i in range (2,Number):
        if Number % i ==0:
            break
    print("yes it is a prime number ")

elif Number == 0:
    print ("no it is not a prime number ")

else :
    print ("it is not a prime number")




#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

for Num in range (2,10001):
    if Num > 1 :
        for i in range(2,10000):
            if Num % i ==0:
                break
    else:
        print(Num)
