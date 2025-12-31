#Number guessing game (simple version):
#Secret number = 7
#Let user guess (use while loop) until they guess correctly.
#After each wrong guess print "Too high" or "Too low".
Secret_number=7
guess_number=int(input("guess a number:"))
while (guess_number!=Secret_number):
    
    if (guess_number>Secret_number):
        print("Too high")
        
    elif (guess_number<Secret_number):
        print("Too Low")
    else:
        break
    guess_number=int(input("guess a number:"))
print("Yes the answer is correct!")
