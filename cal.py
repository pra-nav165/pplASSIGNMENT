import  math
a=(float(input("give first value:-")))
sig=(str(input("give oprator")))
b=(float(input("give second value:-")))
add=a+b
s=a-b
m=a*b
q=a//b
r=a%b
d=a/b
F=int(input("eanter number whis factorial you want:-"))
    
if sig=="+":
   print("a+b=",add)
elif sig=="-":
   print("a-b=",s)
elif sig=="-":
   print("a*b=",m)
elif sig=="-":
   print("a//b=",q)
elif sig=="-":
   print("a% b=",r)
elif sig=="-":
   print("a/b=",d)

elif sig=="^":
   print(math.pow(a,b))

elif sig=="!":
   result=1
for i in range(1,F):
 x=i*1+i
 print(x)
else:
   print("error")



