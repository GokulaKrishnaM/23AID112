#Ask user for two exam scores (0–100).
#Print "You passed!" if both scores are ≥ 50, otherwise "You need to retake some exams".
score_1=int(input("Score 1:"))
score_2=int(input("Score 2:"))
if (50<=score_1<=100 and 50<=score_2<=100):
    print("You passed!")
else:
    print("You need to retake some exams")