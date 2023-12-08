import random

class Simulation:
    """
    Monty Hall Simulation Class.

    Simulation should take an attribute, an integer, which represents the amount of doors that the
    simulation will use to play the game.

    Attributes:
        numdoors - An integer; the number of doors that will be used to play the game.

    Methods:
        __init__(self, doornum):
            Initializes the Simulation instance with the specified number of doors.

        set_random_doors(self):
            Sets up a random configuration of doors, placing a car behind one of them and zonks behind the rest.

        choose_doors(self):
            Simulates the contestant's choice and the host's opening of a door with a zonk, providing the remaining doors.

        play_game(self, switch=False, iterations=1):
            Plays the Monty Hall game for a specified number of iterations and returns the win percentage.

    """
    def __init__(self, doornum  ):
        self.numdoors = doornum  

    def set_random_doors(self):
        """
        Sets up a random configuration of doors.
        Parameters:
            self
        Returns:
            list: A list representing the doors, with a car behind one door and zonks behind the others.
        """
        doors = ["zonk"] * self.numdoors
        car_index = random.randint(0, self.numdoors - 1)
        doors[car_index] = "car"
        return doors

    def choose_doors(self):
        """
        Simulates the choice and the opening of a door with a zonk.

        Returns:
            tuple: A tuple containing the contestant's chosen door and the alternate door.
        """

        doors = self.set_random_doors()
        contestant_door = random.choice(doors)
        doors.remove(contestant_door)
        doors.remove("zonk")
        alternate_door = random.choice(doors)
        return contestant_door, alternate_door

    def play_game(self, switch=False, iterations=1):
        """
        Plays the Monty Hall game for a specified number of iterations and returns the win percentage.

        Args:
            switch (bool): Default value of False; Determines whether a contestant decides to
                switch their door when playing the game and given the option to do so. This value will
                not change over time, if the value is False it will remain so through all iterations of game played
            iterations (int): The number of times that a person will play
                the game. Each time they play a game the doors should be random, and the choices
                should be random

        Returns:
            float: The win percentage as a decimal.
        """
        if iterations <= 0:
            raise ValueError("Number of iterations must be greater than zero.")

        wins = 0
        for _ in range(iterations):
            contestant_door, alternate_door = self.choose_doors()

            if (contestant_door == "car" and not switch) or (alternate_door == "car" and switch):
                wins += 1

        win_percentage = wins / iterations if iterations > 0 else 0
        return win_percentage

if __name__ == "__main__":
    # Test the simulation with switching doors for 1,000 iterations
    simulation = Simulation(3)
    switch_iterations = 1_000
    win_percentage = simulation.play_game(switch=True, iterations=switch_iterations)

    print(f"Win percentage with switching doors over {switch_iterations} iterations: {win_percentage:.2%}")
