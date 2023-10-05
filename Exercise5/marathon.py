import players as player
"""

Driver: Danyil Butkovskyi
Navigator: Joelle Mbella Banim
Assignment: Exercise: Marathon
Date: 10_05_23

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def play_games():
    """
    Play_games
    Args: None
    returns tuple of name and number of iterations over the list
    """
    i = 0
    players_list = []
    while(i < 3):  
        red_player = player.RedPlayer("RedPlayer" + str(i))
        blue_player = player.BluePlayer("BluePlayer" + str(i))
        players_list.append(red_player)
        players_list.append(blue_player)
        i+=1

    flag = True
    iteration_count = 0
    while flag:
        winner = None
        for p in players_list:
            p.walk()
        iteration_count += 1
        for p in players_list:
            if p.position < 1000: # check if player run 1000 steps, if not keep running
                pass
            else:
                flag = False
                winner =  p.name, iteration_count
                break
    return winner
                

if __name__ == "__main__":
    name, iteration_num = play_games()
    print (name)
    print(iteration_num)