"""1. Write a Python Program to Find LCM?
2. Write a Python Program to Find HCF?
3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
4. Write a Python Program To Find ASCII value of a character?"""


#1. Write a Python Program to Find LCM?

def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

Num1 = int(input("Enter first number here : "))
Num2 = int(input("Enter second number here : "))

print("The L.C.M. is", compute_lcm(Num1, Num2))

#2. Write a Python Program to Find HCF?

def find_hcf(x,y):
    if x > y:
        smaller = y

    else:
     smaller = x

    for i in range(1,smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
num1 = int(input("Enter first number here : "))
num2 = int(input("Enter second number here : "))
if num1<0 or num2<0:
    print("please enter positive number ")

else :
    print("the hcf is ",find_hcf(num1,num2))



#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

Dec_val = int(input("Please enter your decimal value here : "))

print("The decimal value of ", Dec_val , "is")
print((bin(Dec_val)) , "in binary" )
print((oct(Dec_val)), "in octal ")
print((hex(Dec_val)), "in hexadecimal")



#4. Write a Python Program To Find ASCII value of a character?

Char = input("Enter character here to find its ASCII value : ")

print("The ASCII value of ", Char , "is" ,ord(Char))




