# Computer Quiz Game: CFG Degree quiz

print("Welcome to my quiz game!")

playing = input("Do you want to know if you are ready to take CFG Degree: Software Engineering boot camp course? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's proceed. ")
score = 0

answer = input("Do you want to earn a recognised certificate that can help you land a job as a software engineer? ")
if answer.lower() == "yes":
    print('Great!')
    score += 1
else:
    pass

answer = input("Are you available & willing to commit 3 hours every evening Monday to Thursday attend an online class? ")
if answer.lower() == "yes":
    print('Great!')
    score += 1
else:
    pass

answer = input("Can you commit to self-study outside of these online classes to catch up, do homework & projects? ")
if answer.lower() == "yes":
    print('Wonderful!')
    score += 1
else:
    pass

answer = input("Do you have experience / knowledge of SQL & Python? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    pass

if score == 0:
    print("It looks like you are not ready yet and that's okay :) Keep this opportunity in mind and try to prepare for the next CFG Cohort to ensure that you maximise the opportunity.")
elif score == 1 or score == 2:
    print("It looks like you are ready but needs some more time. Perhaps reflect on your goals, and review your time management to ensure that you maximise the CFG Degree")
else:
    print("Wonderful! It looks like you are ready to take the CFG Degree!")