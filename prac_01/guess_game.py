
SECRET_NUMBER = 6

guess = 0

while guess != SECRET_NUMBER:
    guess = int(input("Guess the secret number between 1 and 10: "))

    if guess == SECRET_NUMBER:
        print(" Correct!")
    else:
        print(" Wrong! Try again.")