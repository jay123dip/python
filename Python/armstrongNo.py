num = int(input('Enter the number: '))
no_of_digit=0
temp = num
while temp>0:
    no_of_digit=no_of_digit+1
    temp=temp//10

temp = num
sum=0
while temp>0:
    rem=temp % 10
    sum=sum+(rem**no_of_digit)
    temp=temp//10
    
if sum==num:
    print("{} is Armstrong number".format(num))
else:
    print('{} is not a Armstrong number'.format(num))