def getGuess():
    guess = int(input("Enter a guess: "))
    return guess


def main():
    guess = getGuess()
    if guess == 50:
        print ("Correct")
    else:
        print("Incorrect")
        
    
main()