from rps2 import rps
#from rps1 import rps
import pytest


"""
test function, takes no arguments
Checks if function rps from the imported module returns the expected value 
"""
def test_rps():
    assert rps("scissors", "scissors") == 0
    assert rps("rock", "rock") == 0
    assert rps("paper", "paper") == 0
    assert rps("scissors", "paper") == 1
    assert rps("paper", "rock") == 1
    assert rps("rock", "scissors") == 1
    assert rps("scissors", "rock") == 2
    assert rps("rock", "paper") == 2
    assert rps("paper", "scissors") == 2