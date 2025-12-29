#Create a list with 8 random integers between 1–100.
#Find and print:
#the biggest number
#the smallest number (without using max() / min() functions – use loop and variables)
import random
numbers=[]
for i in range(8):
    numbers.append(random.randint(1,101))
print (numbers)
