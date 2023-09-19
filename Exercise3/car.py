import math 

class Car:
    def __init__ (self, x = 0.0, y= 0.0, heading = 0.0):
        """ creates instance of car
    
        Attributes:
        self: the car object.
        x: the starting x coordinate of the car, as a float. Default: 0.
        y: the starting y coordinate of the car, as a float. Default: 0.
        heading: the starting heading, as a float. Default: 0.
        """
        self.x = x
        self.y = y
        self.heading = heading
        

    def turn(self, degrees):
        """ does turn
    
        Attributes:
        self: the car object.
        degrees: number of degres to turn 
        """
        self.heading += degrees
        self.heading = ((self.heading) % 360)

    def drive(self, distance):
        """ drives distance
    
        Attributes:
        self: the car object.
        distance: float to move
        """
        heading = math.radians(self.heading)
        self.x += distance * math.sin(heading)
        self.y -= distance * math.cos(heading)

def sanity_check():
    """ does check: turn, drive, turn, drive
    
    Attributes: none
    Return: car instance
    """
    car1 = Car()
    car1.turn(90)
    car1.drive(10)
    car1.turn(30)
    car1.drive(20)
    print(f"Location: {car1.x}, {car1.y}")
    print(f"Heading: {car1.heading}")
    return car1

if __name__ == "__main__":
    sanity_check()

