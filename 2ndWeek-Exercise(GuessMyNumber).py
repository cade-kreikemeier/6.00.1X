guess = 0

secretNum = input('Please think of a number between 0 and 100!n/')
if secretNum not in range(0,100):
    print("I'm sorry, that is not a valid answer.")
    secretNum = input('Please think of a number between 0 and 100!n/')

ans = input("Is your secret number " + str(guess) "?n/Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if ans != 'c' or 'h' or 'l':
    print('Sorry, I did not understand your input.')