import pandas as pd
import seaborn as sns
from monty_hall import Simulation

class Plot:
    """
    Monty Hall Simulation Visualization Class.

    This class stores data for a particular instance of a simulation of the Monty Hall problem and
    provides functionality to export a visualization of the win percentages.

    Attributes:
        doors (int): The number of doors that the simulation is based on.
        iterations (int):  The number of iterations that a simulation will be based on.
        sequence (list): Starts empty, is later populated by dictionaries each containing: num of
            iterations a game was played, percentage won for that simulation, doors used in that
            simulation, whether the door was switched or not for that simulation.

    Methods:
        __init__(self, doors=3, iterations=200):
            Initializes the Plot instance with the specified number of doors and iterations.
            Automatically generates a sequence of simulation results and exports a visualization.

        make_plot(self):
            Creates a pandas DataFrame from the sequence attribute and generates a seaborn
            lmplot for visualization. The plot is saved as a PNG file with a dynamically generated filename.
    """
    def __init__(self, doors=3, iterations=200):
        """
        Initialize the Plot instance with default or specified parameters.

        Args:
            doors (int): Defaults to 3; The number of doors that the simulation will be based on.
            iterations (int): Defaults to 200; The number of iterations that a simulation will be based on.
        """
        self.doors = doors
        self.iterations = iterations
        self.sequence = []

        for i in range(1, iterations + 1):
            simulation = Simulation(doors)
            switched = i % 2 == 0
            win_percentage = simulation.play_game(switch=switched, iterations=i)
            
            simulation_info = {
                "iterations": i,
                "percentage": win_percentage,
                "doors": doors,
                "switched": str(switched)
            }
            self.sequence.append(simulation_info)

        self.make_plot()

    def make_plot(self):
        df = pd.DataFrame(self.sequence)
        plot = sns.lmplot(x="iterations", y="percentage", data=df, hue="switched", fit_reg=False)
        plot.set(title=f"Monty Hall Simulation - {self.doors} doors, {self.iterations} iterations")
        plot.savefig(f"monty_hall_{self.doors}_doors_{self.iterations}_iterations.png")
        print("Visualization exported successfully.")

if __name__ == "__main__":

    plot_instance = Plot(doors=5, iterations=100)