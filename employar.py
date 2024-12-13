employ=[]
A_group=[]
B_group=[]
number_of_employs=int(input("number of employ"))
for id in range(number_of_employs):
 id=int(input("enter id of emply"))
 employ.append(id)
for id in employ:
 if id%2==0:
  A_group.append(id) 
 else:B_group.append(id)
EIDS=int(input("emter your employ id"))
if EIDS in A_group:print("you ane a part of group A")
elif EIDS in B_group:print("you are a paet of group B")
else: print("invaled ID")


