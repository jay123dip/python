# print first n number from fibonacci series
number = int(input('First how many numbers you want to print in fibonacci series ? please Enter the number : '))

i = 0
first_number = 0
second_number = 1

for i in range(0,number + 1):
    if i <= 1:
        next = i
    else:
        next = first_number + second_number
        first_number = second_number
        second_number = next
    print(next,end=' ')