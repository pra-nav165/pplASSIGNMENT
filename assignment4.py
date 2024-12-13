num=[]
num=list(input("write the number you want to check:-"))
num1=int(num[0])
num2=int(num[1])
num3=int(num[2])
GN=num1*100+num2*10+num3
AN=num1**3+num2**3+num3**3
print(AN,GN)
if AN==GN:
    print(GN,"is an armstrong number")
else:print(GN,"is not an armstrong number")
