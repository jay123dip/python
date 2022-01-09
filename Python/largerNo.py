# largest from three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2 and num1 > num3):
          print("{0} is Greater Than both {1} and {2}". format(num1, num2, num3))
elif (num2 > num1 and num2 > num3):
          print("{0} is Greater Than both {1} and {2}". format(num2, num1, num3))
elif (num3 > num1 and num3 > num2):
          print("{0} is Greater Than both {1} and {2}". format(num3, num1, num2))
else:
          print("Either any two numbers or all the three numbers are equal")


# largest of two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1>num2:
#     print("{} is greater than {}".format(num1,num2))
# elif num1==num2:
#     print('Numbers are equal ')
# else:
#     print("{} is greater than {}".format(num2,num1))
