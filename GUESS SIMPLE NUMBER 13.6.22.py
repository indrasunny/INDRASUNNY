import random

def main():
    """Start a number guessing game between 1 - 10."""
    print("Guess the number!")

    x = random.randint(1, 10)
    guess = None

    while x != guess:

        guess = int(input("Pick a number between 1 to 10: "))
        
        if x == guess:
          print("You genius!")
            break
        else: 
            print("Try Again")

main()
