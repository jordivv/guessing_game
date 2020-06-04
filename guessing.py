number = 43;

print('Guess a number')
guess = input()


def higher_lower(a_guess):
    if int(guess) > int(number):
        print("your number is too high");
    if int(guess) < int(number):
        print("your number is too low")

while guess.isdigit() == True:
    if int(guess) == int(number):
        print("Correct! you guessed the number")
        break
    else:
        higher_lower(guess)
        print('Guess a number')
        guess = input()

while guess.isdigit() != True:
    print("please enter an integer - non integers are not allowed")
    print('Guess a number')
    guess = input()
    while guess.isdigit() == True:
        if int(guess) == int(number):
            print("Correct! you guessed the number")
            break
        else:
            higher_lower(guess)
            print('Guess a number')
            guess = input()