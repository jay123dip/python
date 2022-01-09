number = int(input('Enter the integer Number: '))

temp = abs(number)
count_digit = 0
while temp > 0:
    temp = temp // 10
    count_digit = count_digit + 1

print('Number of digits in {} is {}'.format(number,count_digit))