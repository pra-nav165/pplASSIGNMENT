def my_data_type(user_input):
    try: 
        return int(user_input)
    except: ValueError
    pass
    try: 
        return float(user_input)
    except: ValueError
    pass
    try: 
       return str(user_input)
    except: ValueError
    pass
    try: 
       return list(user_input)
    except: ValueError
    pass
    return user_input
user_input=input("give input in singal data type:- ")
a=my_data_type(user_input)
if type(a)==int: 
    print("int")
elif type(a)==float:
    print("float")
elif type(a)==str:
    print("string")
elif type(a)==list:
    print("list")
else:
    print("error")

