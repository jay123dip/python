principle=float(input("Enter the principle amount: "))
roi = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in year: "))

SI =(principle*roi*time)/100
print('simple interest for principle amount{}={}'.format(principle,SI))
