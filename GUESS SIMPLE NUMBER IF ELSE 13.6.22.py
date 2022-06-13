import random

def main():
    """Start a number guessing game between 1 - 10."""
    print("Guess the number!")

    x = random.randint(1, 10)
    guess = None # None merujuk nombor yang kosong bukan nilai 0 int

    while x != guess: # merujuk bukan/salah  nilai x guess arahan menentukan syarat no lebih besar atau kecil

        guess = int(input("Pick a number between 1 to 10: "))
        
        if x == guess:
            print("You genius!")
            break
        else: 
            print("Try Again")


main()
