import random


def get_random_number(start: int, end: int):
    return random.randint(start, end)


def ask_user_to_guess(start: int, end: int):
    guess = 0
    try:
        guess = int(
            input(f'Guess a number between {start} and {end} inclusive: '))
        if (guess < start or guess > end):
            raise AssertionError

    except ValueError:
        print('Only integers allowed!')

    except AssertionError:
        print(f'Your guess is out of range')

    return guess


def get_result(user_number: int, number_to_guess: int) -> str:
    if user_number < number_to_guess:
        return 'Too Low'
    if user_number > number_to_guess:
        return 'Too High'
    if user_number == number_to_guess:
        return 'Just Right'


def loop_game(game):
    while True:
        ans = game()
        if (ans == 'n'):
            return


def ask_user_to_play_again():
    ans = input('Do You want to try again ? (y/n)')
    return ans.lower()


def play_game():
    user_lives = 3
    start = 0
    end = 15

    number_to_guess = get_random_number(start, end)

    while True:
        user_number = ask_user_to_guess(start, end)
        result = get_result(user_number, number_to_guess)

        if (result == 'Just Right'):
            print('Just Right!')
            return ask_user_to_play_again()

        user_lives -= 1

        if user_lives == 0:
            print('Sorry You didn\'t guess in time!')
            return ask_user_to_play_again()

        elif user_lives == 1:
            print(f'You have {user_lives} guess left')

        else:
            print(f'You have {user_lives} guesses left')

        print(result)


if __name__ == "__main__":
    loop_game(play_game)
