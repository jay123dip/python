units = float(input("Enter the units: "))
if units<50:
    amount=50*2.60
    surCharge=25
elif units<=100:
    amount=130+((units-50)*3.25)
    surCharge=35
elif units<=200:
    amount=130+162.50+((units-100)*5.25)
    surCharge=45
else:
    amount=130+162.50+526+((units-200)*8.45)
    surCharge=75

total_amount=amount+surCharge
print('\nElectricity Bill = %.2f' %total_amount)