number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
a = number1
b = number2
while(number2 != 0):
    temp = number2
    number2 = number1 % number2
    number1 = temp

gcd = number1   
print(" GCD of {0} and {1} = {2}".format(a, b, gcd))

lcm = (a*b)/gcd
print(" LCM of {0} and {1} = {2}".format(a, b, lcm))

