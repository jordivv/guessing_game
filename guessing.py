# number that the user has to guess
number = 47;

# initial instructions
print('Guess a number')
guess = input()


# function determining if the number entered by the user is larger or smaller than the desired number
def higher_lower(a_guess):
    if int(guess) > int(number):
        print("your number is too high");
    if int(guess) < int(number):
        print("your number is too low")

# while loop running while the entered value is a number
while guess.isdigit() == True:
    if int(guess) == int(number):
        print("Correct! you guessed the number")
        break
    else:
        higher_lower(guess)
        print('Guess a number')
        guess = input()

# while loop running while the entered value is not a number
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