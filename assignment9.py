import math
num=int(input("enter a number"))
sqrt=math.sqrt(num)
sq=num**2
cub=num**3
prime="is"
for i in range(2,num):
   if num%i==0:prime="is not"
   else:primr="is"
for num in range(1,num):
   num=num*num-1
print (num)
print(f"number you gave {prime}primr")
