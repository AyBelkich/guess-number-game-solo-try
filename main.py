import random

def game_session():
    secret_number = random.randint(1, 100)

    print("guess the number between 1 and 100")

    attempts = 0

    while True:
        guess_str = input("guess:")

        try:
            guess = int(guess_str)
        except ValueError:
            print("please reenter value")
            continue

        attempts += 1
        
        if guess > secret_number:
            print("too high, attempts used:", attempts)
        elif guess < secret_number:
            print("too low, attempts used:", attempts)
        else:
            print("win in", attempts, "attempts")
            break

def main():
    while True:
        game_session()
        play_again = input("play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("thanks for playing!")
            break

if __name__ == "__main__":
    main()