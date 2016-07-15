from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

print "The lucky number is %i" % random_number
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess != random_number:
        guesses_left -= 1
        print "Wrong! You have %i gusses left." % guesses_left
    elif guess == random_number:
        print "You win!"
        break
else:
    print "You lose."
