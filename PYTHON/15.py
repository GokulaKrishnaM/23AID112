# Create list = [12, 45, 3, 98, 7, 34, 21]
# Use a loop to:
# a) print each number
# b) print only numbers greater than 30
# c) count how many numbers are greater than 30
List=[12,45,3,98,7,34,21]
print("List of all numbers:")
for i in range(len(List)):
    print (List[i])
print("Numbers greater than 30:")
for i in range(len(List)):
    if(List[i]>30):
        print(List[i])
count=0
for i in range(len(List)):
    if(List[i]>30):
        count = count+1
print("Number of numbers greater than 30:",count)