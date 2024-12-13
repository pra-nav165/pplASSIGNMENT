a=input(str("enter your numbers number systum")) 
b=input(str("enter number systum you want"))

 
#desimal to binary
db = []
def func(num_db):
   while num_db > 0:
        gray = num_db %2
        db.append(gray)
        num_db //= 2
   for xdb in reversed(db):
        print(xdb)
   return(xdb)


 #desimal to octal
do = []
def func(num_do):
    while num_do> 0:
        gray = num_do % 8
        do.append(gray)
        num_do //= 8
    for xdo in reversed(do):
        print(xdo)
    return xdo


 #desimal to hexadesimal
dh = []
def func(num_dh):
    while num_dh > 0:
        gray = num_dh % 16
        if gray==10:
          gray="A"
        elif gray==11:
            gray="B"
        elif gray==12:
            gray="C"
        elif gray==13:
            gray="D"
        elif gray==14:
            gray="E"
        elif gray==15:
            gray="F"
            
          
        dh.append(gray)
        num_dh //= 16
    for xdh in reversed(dh):
        print(xdh)
    return xdh


if b=="binary":
  num_db = int(input("Enter the number: "))
  func(num_db)
elif b=="octal":
  num_do = int(input("Enter the number: "))
  func(num_do)
if b=="hexadeimal":
 num_dh = int(input("Enter the number: "))
 func(num_dh)
