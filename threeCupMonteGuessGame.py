# '''3 Cup Monte is a 3 cup shuffling game In which there is a ball hidden in one of the cup 
# and the user has to guess which cup has the ball If the user guesses it right then user is the winner!
# '''

# #The random module has been imported and shuffle is used

# import random

from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)   # this requires a return function so taht it can be assigned to new result variabble
    return mylist     # By using the return function the list can be shuffled repeatedly each time



def player_guess():
    
    guess = ''
    
    while guess not in ['0','1','2']:

        guess = input("Pick a number: 0,1, or 2")
        
    return int(guess)



def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('CORRECT!')
    else:
        print("Wrong guess!")
        print(mylist)



# now calling all the functions 

#initial list

mylist =[' ','O',' ']   # The letter O represent as a ball And the three items are to be represented as cups

# shuffle list

mixedup_list = shuffle_list(mylist)    # goal is to shuffle the letter O as ball in the list randomly

#USER GUESS

guess = player_guess()   # asks user there input 0, 1 , 2 

#CHECK GUESS

check_guess(mixedup_list,guess)  #returns the shuffled list and whats was user input if wrong!