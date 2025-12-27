#Ask the user for their birth year (as string), convert it to integer, calculate their age in 2025 and print:
#"You will be X years old in 2025!" (X = 2025 - birth_year)
birth_year=str(input("Enter your birth year"))
birth_year=int(birth_year)
age=2025-birth_year
print("You will be ", age, "years old in 2025!")
