xs=[]
gray=0
def func(num):
    while num>0:
        gray=num%8
        num//=8 
    xs.append(gray)
    for x in reversed(xs):
        print(xs)
     
    
    return x
num=int(input("enter the number"))
func(num)