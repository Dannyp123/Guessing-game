import random
from termcolor import colored
import time


def main():
    print(colored('Welcome to the guessing game!', 'yellow'))
    print(colored('Please guess a number from 1 - 100!', 'yellow'))
    random_num = random.randint(1, 100)

    guesses_remaining = 6
    while True:
        user_num = int(input('Guess a number: '))
        if user_num > 100 or user_num < 0:
            print('Number must be between 1 and 100')
            continue
        guesses_remaining = guesses_remaining - 1
        if user_num == random_num:
            print(
                colored('Yay You got it, you are very good at this!!!',
                        'green'))
            exit()

        else:
            if random_num > user_num:
                print(colored("Choose Higher", 'cyan'))
            elif random_num < user_num:
                print(colored("Choose Lower", 'cyan'))

        if guesses_remaining == 0:
            print(colored('Sorry.... Ran out of tries', 'red'))
            print('The winning number was: ', random_num)
            print('BUUUUUUUUUUUUUUT.......')
            time.sleep(3)
            break

    random_num2 = random.randint(1, 25)
    guesses_remaining_redemption_round = 4
    while True:

        num = int(
            input(
                colored('Redemption Round...What is your guess 1-25: ',
                        'yellow')))

        guesses_remaining_redemption_round = guesses_remaining_redemption_round - 1

        if num == random_num2:
            print('SUCCESS!!')
            break

        if guesses_remaining_redemption_round == 0:
            print(colored('Womp, womp, womp, wooooommmmmp :-( !!', 'red'))
            print('The winning number was: ', random_num2)
            break

        else:
            if num > random_num2:
                print(colored('REALLY.... guess lower!', 'cyan'))
            elif num < random_num2:
                print(colored('Guess a little bit higher my guy!', 'cyan'))


if __name__ == '__main__':
    main()
