#Ask user for two numbers (as strings), convert them to integers, then print:
#their sum
#their difference
#their product
#which one is bigger (or if they are equal)
num1=str(input("Number 1: "))
num2=str(input("Number 2: "))
num1=int(num1)
num2=int(num2)
sum=num1+num2
diff=num1-num2
product=num1*num2
print("Sum =",sum)
print("Difference =",diff)
print("Product =",product)
if(num1>num2):
    print(num1,"is greater than",num2)
elif(num1==num2):
    print("both the numbers are equal")
else:
    print(num2,"is greater than",num1)
    