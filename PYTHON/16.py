#Create list of numbers 1–20.
#Print only numbers that are divisible by 3 (use %).
numbers=list(range(1,21))
for i in range(len(numbers)):
    if (numbers[i]%3==0):
        print(numbers[i])