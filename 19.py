#Create this list:
#grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
#Count how many students:
#got A (≥90)
#got B (80–89)
#got C (70–79)
#got below 70
grades=[85,92,78,65,88,91,73,89,55,94]
count_A=0
for i in grades:
    if i>=90:
        count_A=count_A+1
print("Number of students whose grade is A:",count_A)
count_B=0
for i in grades:
    if 90>i>=80:
        count_B=count_B+1
print("Number of students whose grade is B:",count_B)
count_C=0
for i in grades:
    if 80>i>=70:
        count_C=count_C+1
print("Number of students whose grade is C:",count_C)
count_D=0
for i in grades:
    if i<70:
        count_D=count_D+1
print("Number of students whose grade is below 70:",count_D)