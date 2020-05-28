''' 

###########################################               DOCUMENATION                     ################################################################

This is the CLI version of Rock, Paper, Scissors game. Sadly it doesn't inclde fancy graphics since I am new to programming !
Some of the Commands of the game are as follows != 

1. 1 stands for Stone

2. 2 stands for Paper 

3. 3 Stands for Scissors

The mechanics of the Game is very simple. Here in brief --> Firstly the input is being taken and then using if-else loop it prints

what you entered basically its convert the numerical value into characters. Then using the random library the cpu also generates some

random numbers between 1 and 3 and then using this numbers I used again a if-else loop to match and the results and declare where

the gamers win or lose it.

Hope you understand the Mechanics !

# To play the game just install python 3.8 or above

Install python using conda

$ sudo conda install python=3.8


'''

# Importing Important library

import math
import random

print('Rules of the Game are ----> \n (i)   1 stands for Stone \n (ii)  2 stands for Paper \n (iii) 3 Stands for Scissors') # Rules !

players_input = int(input('Enter Your Move ---------> ')) # Taking user input 

# The preprocess function in which the numbers gets converted into Character for user readibility

def preprocess():
    if players_input == 1:
        print('You entered Stone.')
        print('CPU is Thinking ...................................................')

    elif players_input == 2:
        print('You entered Paper.')
        print('CPU is Thinking ...................................................')

    elif players_input == 3:
        print('You entered Scissors.')
        print('CPU is Thinking ...................................................')

    else:
        print("Sorry ! You entered something the CPU can't process. Try again.")
        print('Exiting the Game !')
        exit()

preprocess() 


cpu_move = random.randint(1,3) # Generating random number


# Converting the generated random number into rock paper or scissors


def cpumove():
    if cpu_move == 1:
        print('CPU thought Stone !')
    elif cpu_move == 2:
        print('CPU thought Paper !')
    elif cpu_move == 3:
        print('CPU thought Scissor !')

cpumove()

# The Decision making loop which decides whether the player won the game or not 

def game():
    if players_input == 1 and cpu_move == 3:
        print('You Win !')
    elif players_input == 1 and cpu_move == 2:
        print('You Lose')
    elif players_input == 1 and cpu_move == 1:
        print('Match Draw !')    
    elif players_input == 2 and cpu_move == 3:
        print('You Lose !')
    elif players_input == 2 and cpu_move == 1:
        print('You Lose !')
    elif players_input == 2 and cpu_move == 2:
        print('Match Draw !')
    elif players_input == 3 and cpu_move == 1:
        print('You Lose !')
    elif players_input == 3 and cpu_move == 2:
        print('You Win !')
    elif players_input == 3 and cpu_move == 3:
        print('Match Draw !')

game()

# Game Loop for retrying !

counter = 0

restart = input("Wanna play the game again ? \n")

while counter == 0:    # The loop for retrying the game again and again Setup a infinite loop


    if restart == 'Yes' or restart == 'y':
        players_input = int(input('Enter Your Move ---------> '))
        preprocess()
        cpumove()
        game()
        restart = input("Wanna play the game again ? \n")
    else:
        print('Exiting the Game! Hope you enjoyed the Game.')
        exit() # Exiting the Game
