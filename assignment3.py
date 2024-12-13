course1=float(input("marks of first corse"))
course2=float(input("marks of second corse"))
course3=float(input("marks of third corse"))
course4=float(input("marks of forth corse"))
course5=float(input("marks of fifth corse")) #to get the marks from user

# Check if student passes all courses
if course1 >=40 and course2>=40 and course3>=40 and course4>=40 and course5>=40:
    # Compute aggregate percentage
    aggregate = (course1+course2+course3+course4+course5)/ 5

    if aggregate > 75:
        grade = "Distinction"
    elif aggregate >= 60:
        grade = "First class"
    elif aggregate >= 50:
        grade = "Second class"
    elif aggregate >= 40:
        grade = "Pass class"
    else:
        grade = "Fail"
else:print("gread:fail")

print ("Aggregate:",aggregate)
print ("Grade:",grade)    