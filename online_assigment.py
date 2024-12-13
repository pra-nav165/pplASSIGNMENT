n = int(input("Enter the total number of students: "))
marks_students = []

for i in range(n):
    marks = float(input("Enter the marks for the students: "))
    marks_students.append(marks)

ts = 0
ls =25
for i in marks_students:
    if i>ts:
        ts=i
    if i<ls:
        ls=i
ps = 0
fs = 0

for i in marks_students:
    if i >= 12:
        ps += 1
    else:
        fs += 1

print(ts)
print(ls)
print(ps)
print(fs)
