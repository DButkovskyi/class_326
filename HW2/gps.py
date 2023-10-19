import sys
import argparse

class City:
    """A class representing a city on a map.

    Attributes:
        name (str): The name of the city.
        neighbors (dict): A dictionary of neighboring cities and their associated distances and interstate information.

    Methods:
        __init__(self, name): Initialize a City instance with a name.
        __repr__(self): Return a string - name of the City.
        add_neighbor(self, neighbor_city, distance, interstate): Add a neighboring city with distance and interstate information.

    """
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
    
    def __repr__(self):
        return self.name

    def add_neighbor(self, neighbor_city, distance, interstate):
        if neighbor_city not in self.neighbors:
            self.neighbors[neighbor_city.name] = (distance, interstate)
        if self.name not in neighbor_city.neighbors:
            neighbor_city.neighbors[self.name] = (distance, interstate)
            
class Map:
    """A class representing a map with cities and routes.

    Attributes:
        cities (list): A list of City instances.

    Methods:
        __init__(self, relationships): Initialize a Map with city relationships.
        __repr__(self): Return a string representation of the Map.
        get_city_by_name(self, name): Get a City instance by name. I decoded to make my life a little easier and create function to get CIty by name.
    """
    def __init__(self, relationships):
        self.cities = []

        for city_name, neighbors_data in relationships.items():
            city = self.get_city_by_name(city_name)

            if city is None:
                city = City(city_name)
                self.cities.append(city)

            for neighbor_name, distance, interstate in neighbors_data:
                neighbor = self.get_city_by_name(neighbor_name)

                if neighbor is None:
                    neighbor = City(neighbor_name)
                    self.cities.append(neighbor)

                city.add_neighbor(neighbor, distance, interstate)

    def __repr__(self):
        return ', '.join(repr(city) for city in self.cities)
    
    def get_city_by_name(self, name):
        for city in self.cities:
            if city.name == name:
                return city
        return None
    

def bfs(map, start, goal):
    """Perform a Breadth-First Search (BFS) to find a route from a starting city to a destination city on a map.

    Args:
        map (Map): The Map instance representing the map.
        start (str): The name of the starting city.
        goal (str): The name of the destination city.

    Returns:
        list or None: A list of instructions for the route or None if no path is found.

    """
    explored = []
    queue = [[start]]

    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbors = map.get_city_by_name(node).neighbors.keys()

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)

                queue.append(new_path)

                if neighbor == goal:
                    return [map.get_city_by_name(city).name for city in new_path]

            explored.append(node)

    return None

def main(starting_city, destination_city, connections):
    """Main function to find and provide route instructions between two cities on a map.

    Args:
        starting_city (str): The name of the starting city.
        destination_city (str): The name of the destination city.
        connections (dict): A dictionary representing city relationships and distances.

    Returns:
        str: Instructions for the route or a message indicating no path was found.

    """
    map_object = Map(connections)
    instructions = bfs(map_object, starting_city, destination_city)
    if instructions:
        output = ''
        for i, city in enumerate(instructions):
            if i == 0:
                print(f"Starting at {city}")
                output += f"Starting at {city}\n"
            if i < len(instructions) - 1:
                next_city = instructions[i + 1]
                current_city = map_object.get_city_by_name(city)
                next_neighbor = current_city.neighbors[next_city]
                distance, interstate = next_neighbor
                print(f"Drive {distance} miles on {interstate} towards {next_city}, then")
                output += f"Drive {distance} miles on {interstate} towards {next_city}, then\n"
            else:
                print("You will arrive at your destination")
                output += "You will arrive at your destination"
        return output
    print("No path found.")
    return "No path found."


###############################################

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--starting_city', type = str, help = 'The starting city in a route.')
    parser.add_argument('--destination_city', type = str, help = 'The destination city in a route.')
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    
    connections = {  
        "Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
        "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")], 
        "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
        "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
        "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
        "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
        "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
        "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
        "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
        "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
        "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
        "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
        "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
        "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27") ],
        "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
        "Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"), ("Nashville", 180, "40"), ("Ashville", 116, "40")],
        "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
        "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
        "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
        "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
        "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
        "Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
        "Youngstown":[("Pittsburgh", 67, "76")],
        "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")],
        "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
        "Bedford": [("Pittsburg", 107, "76")], #COMEBACK
        "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
        "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
        "Scranton": [("Syracuse", 130, "81")],
        "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }
    
    args = parse_args(sys.argv[1:])
    main(args.starting_city, args.destination_city, connections)

