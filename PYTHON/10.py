#Temperature converter + advice:
#Ask user for temperature in Celsius.
#Convert to Fahrenheit (°F = °C × 9/5 + 32)
#Then print advice:
#< 0 → "Very cold! Wear thick jacket"
#0–15 → "Cold. Wear jacket"
#16–25 → "Nice weather"
#>25 → "Hot! Stay hydrated"
temp_C=float(input("temperature in Celcius:"))
temp_F=(temp_C*(9/5))+32
print("Temperature in Fhrenheit is ",round(temp_F,2))
if(temp_C<0):
    print("Very cold! Wear thick jacket")
elif(0<=temp_C<=15):
    print("Cold. Wear jacket")
elif(16<=temp_C<=25):
    print("Nice weather")
elif(temp_C>25):
    print("Hot! Stay hydrated")