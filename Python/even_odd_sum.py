# print sum of even and odd numbers from 1 to n

last_number = int(input('Enter the number: '))
even=0
odd=0
for i in range(0,last_number+1):
    if i%2==0:
        even=even+i;
    else:
        odd=odd+i
        
print('Sum of Even numbers between 1 to {} is {}'.format(last_number,even))
      
print('Sum of Odd numbers between 1 to {} is {}'.format(last_number,odd))


# print first digit of a number 

# num = int(input('Enter the number: '))
# first_digit = num
# while first_digit>=10:
#     first_digit=first_digit//10
    
# print("First Digit = {}".format(first_digit))