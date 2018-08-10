import random
from termcolor import colored
import time


def welcome():
    print()
    print(colored('\t---------Guessing Game----------', attrs=['bold']))
    print()
    print(colored('*****Hit Enter to began*****', 'red'))
    input()
    print(colored('Please guess a number from 1 - 100!', 'yellow'))


def redemption_round(guesses_remaining_redemption_round):
    random_num2 = random.randint(1, 25)
    print(colored('Redemption Round guess a number from 1 to 25', 'blue'))
    time.sleep(1)
    print()
    print(colored('Hit enter to try one last time!', 'red'))
    input()
    while True:
        num = int(input(colored('What is your guess: ', 'yellow')))
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
            print(colored('Bet that... You Got It!!!', 'green'))
            exit()

        else:
            if random_num > user_num:
                print(colored("Up it up a little bit!", 'cyan'))
                print()
            elif random_num < user_num:
                print(colored("PIPE Down my guy!", 'cyan'))
                print()

        if guesses_remaining == 0:
            print('\tThe winning number was: ', random_num)
            print(colored('Sorry.... Ran out of tries', 'red'))
            print()
            print(colored('It is not over just yet......', 'green'))
            print()
            time.sleep(2)
            print(colored('BOOOOOOM', 'green'))
            break


def main():
    welcome()
    guesses_remaining = 5
    first_round(guesses_remaining)
    guesses_remaining_redemption_round = 3
    redemption_round(guesses_remaining_redemption_round)


if __name__ == '__main__':
    main()
