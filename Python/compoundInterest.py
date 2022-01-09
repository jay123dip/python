# Python Program to find Compound Interest

import math

princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))

CI_future = princ_amount * (math.pow((1 + rate_of_int / 100), time_period)) 
compound_interest = CI_future - princ_amount

print("Future Compound Interest for Principal Amount {} = {}".format(princ_amount, CI_future))
print("Compound Interest for Principal Amount {} = {}".format(princ_amount, compound_interest))