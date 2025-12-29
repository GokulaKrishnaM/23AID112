#Create a list with 8 random integers between 1–100.
#Find and print:
#the biggest number
#the smallest number (without using max() / min() functions – use loop and variables)
import random
numbers=[]
for i in range(8):
    numbers.append(random.randint(1,101))
print (numbers)
biggest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if (i>biggest):
        biggest=i
print("The biggest number is:",biggest)
for i in numbers:
    if (i<smallest):
        smallest=i
print("The smallest number is:",smallest)
