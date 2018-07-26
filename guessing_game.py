import random


def main():
    print('Welcome to the guessing game!')
    print('Please guess a number from 1 - 100!')
    random_num = random.randint(1, 100)

    guesses_remaining = 7
    while True:
        user_num = int(input('Guess a number: '))
        if user_num > 100 or user_num < 0:
            print('Number must be between 1 and 100')
            continue
        guesses_remaining = guesses_remaining - 1
        if user_num == random_num:
            print('Yay You got it, you are very good at this!!!')
            exit()

        else:
            if random_num > user_num:
                print("Choose Higher")
            elif random_num < user_num:
                print("Choose Lower")

        if guesses_remaining == 0:
            print('Sorry.... Ran out of tries, the winning number was',
                  random_num)
            break

        random_num2 = random.randint(1, 25)
        guesses_remaining_redemption_round = 3
    while True:
        num = int(input('Redemption Round...What is your guess 1-25: '))
        guesses_remaining_redemption_round = guesses_remaining_redemption_round - 1

        if num == random_num2:
            print('SUCCESS!!')
            break

        if guesses_remaining_redemption_round == 0:
            print('Womp, womp, womp, wooooommmmmp :-( the winning number was',
                  random_num2)
            break

        else:
            if num > random_num2:
                print('Come on dude, guess lower!')
            elif num < random_num2:
                print('Ayyye guess a little bit higher!')


if __name__ == '__main__':
    main()
