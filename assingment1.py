print("pay check")
#to gate the input besic pay and store it in var BP
BP=int(input("your besic pay:- "))
HRA=BP*10/100 #human resource allowance
TA=BP*5/100 #traveling allowance
Total_pay=BP+HRA+TA #total pay before tax
TAX=Total_pay*2/100 #tax is on total pay
IHP=Total_pay-TAX #total pay after tax
print("your ni had salary after tax is:-",IHP) 