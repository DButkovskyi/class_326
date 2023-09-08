"""A template for a python script deliverable for INST326.

Driver: Instructor Gabriel Cruz
Navigator: None
Assignment: Template INST326
Date: 1_24_21

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import os

def determine_winner(p1, p2):
    """Takes 2 strings as arguments
    Args:
    p1 and p2 - strings of hand shape
    Returns:
    winner as string
    """
    #check for all possible combinations for player 1 to win
    if ((p1 == 's') & (p2 == 'p')) | ((p1 == 'p') & (p2 == 'r')) | ((p1 == 'r') & (p2 == 's')):
        return 'player1'
    #check if same shape - return tie
    elif (p1 == p2):
        return 'tie'
    #all other cases player2 wins
    else:
        return 'player2'


def main(player1_name, player2_name):
    """Takes 2 strings as arguments
    Args:
    p1 and p2 - nmae of players
    Returns:
    winner as string
    """
    #list for valid inputs
    valid_input = ['r','s','p']
    """
    function to take inout and check if input is in valid values. Keeps asking for inout intil valid value is entered.
    """
    def take_input(player_name):
        isValidInput = False
        while not isValidInput:
            player_hand_shape = input(f"{player_name} please enter your hand shape: ")
            if player_hand_shape in valid_input:
               isValidInput = True 
            else:
                print("Sorry, invalid input. Valid options: r, s, p. Try again!")
        os.system('cls||clear')
        return player_hand_shape
    #Take input for both players
    p1_hand_shape = take_input(player1_name)
    p2_hand_shape = take_input(player2_name)
    #winner is a string returned from determine winner function
    winner = determine_winner(p1_hand_shape, p2_hand_shape)
    #dictionary for final print
    output_dict = {'tie' : "Tie",
                   'player1' : f"{player1_name} wins!",
                   'player2' : f"{player2_name} wins!"}
    #prints, using key to get value for final output.
    print(output_dict.get(winner))


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments
    Args:
    args_list (list) : the list of strings from the command prompt
    Returns:
    args (ArgumentParser)
    """
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence.
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
    parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.
    
    return args

if __name__ == "__main__":
    
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?

    #It the script is being run as a module, the block of code under this will not beexecuted.
    #If the script is being run natively, the block of code below this will be executed.

    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.

    main(arguments.p1_name, arguments.p2_name)