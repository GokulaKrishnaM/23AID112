#Number guessing game (simple version):
#Secret number = 7
#Let user guess (use while loop) until they guess correctly.
#After each wrong guess print "Too high" or "Too low".
Secret_number=7

while (i!=Secret_number):
    guess_number=int(input("guess a number"))
    if (i>Secret_number):
        print("Too high")
        
    elif (i<Secret_number):
        print("Too Low")
    else:
        print("Yes the answer is correct!")
    

