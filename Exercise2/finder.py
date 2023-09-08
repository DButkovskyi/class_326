import sys
import argparse

HOME_DATABASE = """shoes,floor,8/23/23,10:00am
papers,cubbard,7/23/23,1:00am
picture frames,wall,6/23/23,10:00pm
tshirts,cubbard,1/13/23,9:00am
soccer balls,basket,2/9/22,12:00pm
kitchen tables,floor,3/23/23,4:00pm
cabinets,corner,5/30/23,10:30pm"""


"""
Takes name string as an argument
nmae - String, name of the object to find
return: formatted string of desiresd output line
"""
def main(name):
    array_of_strings = HOME_DATABASE.split('\n')
    # Create lists variables for each element
    item_names = []
    item_locations = []
    dates_last_moved = []
    times_last_moved = []
    # Iterate through the array of strings
    for line in array_of_strings:
        # Split the line by commas
        parts = line.split(',')
        # Check if the line has enough parts (at least 4) to extract the required information
        # Extract and strip the information for each name
        item_name = parts[0].strip()
        item_location = parts[1].strip()
        date_last_moved = parts[2].strip()
        time_last_moved = parts[3].strip()
        # Append the information to the respective lists
        item_names.append(item_name)
        item_locations.append(item_location)
        dates_last_moved.append(date_last_moved)
        times_last_moved.append(time_last_moved)
    if name in item_names:
        return (f'The {name} were found in the {item_locations[item_names.index(name)]} and were placed there on {dates_last_moved[item_names.index(name)]} at {times_last_moved[item_names.index(name)]}')
    else:
        raise ValueError(f'Sorry, could not find your item named {name} within the database')
    

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
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
    parser.add_argument('object', type=str, help="Please enter the name that we are searching for.")
    
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

    print(main(arguments.object))