def main():
    import random

    secret_number = random.randint(1, 10)

    guess = float(input("guess the secret number between 1 and 10: "))

    if guess == secret_number:
        print("you found the secret number")
    if guess >= secret_number:
        print("too high")
    elif guess <= secret_number:
        print("too low")

main()