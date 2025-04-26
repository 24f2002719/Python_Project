import numpy as np
import random
x = int(input("Range Start from"))
y = int(input("Range End"))

guess_no = random.randrange(x,y)

min_guess_no = np.log2(y-x+1)

guess_counter = 0

while min_guess_no > guess_counter:
    guess_counter += 1

    my_guess = int(input("Guess the number: "))
    if (my_guess == guess_no):
        print(f'The number is {my_guess} and you found it right !! in the {guess_counter} attempt')
        break
    elif(guess_counter >= min_guess_no  and guess_no!= my_guess):
        print(f'Oops sorry, The number is {guess_no} better luck next time')
    
    elif(guess_no>my_guess):
        print("Your guess is lesser")
    elif(guess_no<my_guess):
        print("Your guess is higher")







