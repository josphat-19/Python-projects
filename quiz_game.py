print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")