import random
i=random.randint(1,10)
i=6
print('I am thinking of a number between 1 to 10')
print('You have 3 attempts to guess the correct number')
for guessattempt in range (1,4):
    print('Guess Your Attempt: ')
    guess = int(input())
    if guess < i:
        print('Your guess to too Low')
    elif guess > i:
        print('Your guess is too High')
    else:
        break #This condition is the Correct Guess.
if guess == i:
    print('Good job, You guessed the correct number in ' + str(guessattempt) + ' attempt(s),Impressive !!')
else:
    print('Sorry !! You could not guess the correct number. The Number what I was thinking is',str(i),'.')

