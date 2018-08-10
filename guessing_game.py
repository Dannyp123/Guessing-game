import random
from termcolor import colored
import time


def printing_helper():
    print(colored('\tGuessing Game', attrs=['bold']))
    print()
    print(colored('*****Hit Enter to began*****', 'red'))
    input()
    print(colored('Please guess a number from 1 - 100!', 'yellow'))


def redemption_round(guesses_remaining_redemption_round):
    random_num2 = random.randint(1, 25)
    while True:
        num = int(
            input(
                colored('Redemption Round...What is your guess 1-25: ',
                        'yellow')))
        if num > 25 or num < 0:
            print(colored('Number must be between 1 and 25', 'red'))
            print()
            continue
        guesses_remaining_redemption_round = guesses_remaining_redemption_round - 1
        if num == random_num2:
            print()
            print(colored('****SUCCESS!!****', 'blue'))
            break

        if guesses_remaining_redemption_round == 0:
            print(colored('Womp womp, womp, wooooommmmmp :-( !!', 'red'))
            print()
            print('\tThe winning number was: ', random_num2)
            break

        else:
            if num > random_num2:
                print(colored('REALLY.... guess lower!', 'cyan'))
                print()
            elif num < random_num2:
                print(colored('Guess a little bit higher my guy!', 'cyan'))
                print()
                continue


def first_round(guesses_remaining):
    random_num = random.randint(1, 100)
    while True:
        user_num = int(input('Guess a number: '))
        if user_num > 100 or user_num < 0:
            print(colored('\nNumber must be between 1 and 100', 'red'))
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
                print()
            elif random_num < user_num:
                print(colored("Choose Lower", 'cyan'))
                print()

        if guesses_remaining == 0:
            print('\tThe winning number was: ', random_num)
            print(colored('Sorry.... Ran out of tries', 'red'))
            print()
            print(colored('BUUUUUUUUUUUUUUT.......', 'green'))
            print()
            time.sleep(2)
            break


def main():
    printing_helper()
    guesses_remaining = 5
    first_round(guesses_remaining)
    guesses_remaining_redemption_round = 3
    redemption_round(guesses_remaining_redemption_round)


if __name__ == '__main__':
    main()
