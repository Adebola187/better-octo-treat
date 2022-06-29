
answers = {}

answers[5] = format(5)
print(answers)
answers[4] = "B"
print(answers)


for answer in answers:
    if answers[answer] == 3:
        print(answer)
    else:
        print("true")