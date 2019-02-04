high = 100
low = 0
ans = ''
guess = (high + low)/2

print('Please think of a number between 0 and 100!')

while ans != 'c':
    ans = input("Is your secret number " + str(int(guess)) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while str(ans) != 'c' and str(ans) != 'h' and str(ans) != 'l':
        ans = input("Sorry, I did not understand your input.\nIs your secret number " + str(int(guess)) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'h':
        high = int(guess)
        guess = (int(high) + int(low))/2
    elif ans == 'l':
        low = int(guess)
        guess = (int(high) + int(low))/2
    else:
        break

print('Game over. Your secret number was: ' + str(int(guess)))