#Create a simple traffic light simulator:
#Ask user to enter "red", "yellow" or "green".
#Print appropriate action:
#red → "STOP!"
#yellow → "Prepare to stop"
#green → "You can go"
#anything else → "Wrong input!"
signal=str(input("Signal: red/yellow/green red "))
if(signal=="red"):
    print("STOP!")
elif(signal=="yellow"):
    print("Prepare to stop")
elif(signal=="green"):
    print("You can go")
else:
    print("Wrong input!")