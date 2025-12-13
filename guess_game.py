import random

def main():
    secret_number = random.randint(1, 100)

    print("guess the number between 1 and 100")

    while True:
        guess_str = input("guess:")

        try:
            guess = int(guess_str)
        
        except ValueError:
            print("please reenter value")
            continue

        if guess > secret_number:
            print("too high")
        elif guess < secret_number:
            print("too low")
        else:
            print("win")
            break
if __name__ == "__main__":
    main()