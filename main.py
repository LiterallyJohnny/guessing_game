import random

while True:
    # Computer chooses a number between 0 and 10
    computerNumber = random.randint(0,10)

    # Checks if the number the player entered is an integer
    while True:
        try:
            chances = int(input('How many chances would you like to have? Please enter an integer: '))
            break
        except ValueError:
            print('\nPlease input a valid number.\n')

    # Allows the player to choose a number and then checks if it is equal to the computer's number
    while chances != 0:
        # Checks if the player's number is an integer
        while True:
            try:
                playerNumber = int(input('Guess a number: '))
                break
            except ValueError:
                print('\nPlease input a valid number.\n')

        if playerNumber == computerNumber:
            print('\nCorrect!\n')
            break

        elif playerNumber < computerNumber:
            print('\nIncorrect number. The number you chose is lower than the number the computer chose.\n')
            chances = chances - 1

        elif playerNumber > computerNumber:
            print('\nIncorrect number. The number you chose is higher than the number the computer chose.\n')
            chances = chances - 1

    if chances == 0:
        print('You have failed to guess the computer\'s number. The computer\'s number was ' + str(computerNumber) + '.\n')

    while True:
        playAgain = str.lower(input('Would you like to play again? (Y/n): '))
        if playAgain == 'y':
            print()
            break
        elif playAgain == 'n':
            print('Thanks for playing!')
            print('Terminating program...')
            quit()
        else:
            print('Incorrect input.')

    continue
