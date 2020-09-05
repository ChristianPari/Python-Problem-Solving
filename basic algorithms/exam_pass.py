# Write a function that returns that the user passed or failed the exam.
# The function will take in two parameters; users score, required score

def grade_perc(userScore, reqScore):
    userScore = int(userScore[:-1])
    reqScore = int(reqScore[:-1])
    if userScore >= reqScore:
        return("You PASSED the Exam")
    elif userScore < reqScore:
        return("You FAILED the Exam")


print(grade_perc("85%", "85%"))
print(grade_perc("95%", "85%"))
print(grade_perc("75%", "85%"))
