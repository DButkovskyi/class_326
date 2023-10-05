import random
"""

Driver: Danyil Butkovskyi
Navigator: Joelle Mbella Banim
Assignment: Exercise: Marathon
Date: 10_05_23

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

class Player:
    """
    Class Player with two parameters: name(String) and position(int)
    """
    def __init__(self, name):
        self.name = name
        self.position = 0


class RedPlayer(Player):
    """
    Subclass of Player, has its own wals function
    Args: self
    Doesn't return anything, adds random num beyween 1 - 10 to position
    """
    def walk(self):
        self.position += random.randint(1, 10)

class BluePlayer(Player):
    """
    Subclass of Player, has its own wals function
    Args: self
    Doesn't return anything, adds random num beyween 4 - 8 to position
    """
    def walk(self):
        self.position += random.randint(4, 8)


def play_games():
    """
    Play_games
    Args: None
    returns tuple of name and number of iterations over the list
    """
    i = 0
    players_list = []
    while(i < 3):  
        red_player = RedPlayer("RedPlayer" + str(i))
        blue_player = BluePlayer("BluePlayer" + str(i))
        players_list.append(red_player)
        players_list.append(blue_player)
        i+=1

    flag = True # flas is used to run while loop while no players reach needed number for position
    iteration_count = 0
    while flag:
        winner = None
        for p in players_list:
            p.walk()
        iteration_count += 1
        for p in players_list:
            if p.position < 100: # check if player run 100 steps, if not keep running
                pass
            else:
                flag = False #if yes change the flag and break the loop
                winner =  p.name, iteration_count
                break
    return winner
                

if __name__ == "__main__":
    name, iteration_num = play_games()
    print (name)
    print(iteration_num)