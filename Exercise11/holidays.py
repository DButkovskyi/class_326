"""A template for a python script deliverable for INST326.

Driver: Danyil Butkovskyi
Navigator: None
Assignment: Exercise 11, Holidays
Date: 11_22_23

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from argparse import ArgumentParser
import requests
import sys

def get_holidays(countrycode, year):
    """ Makes get requests to get list of holidays for certain year and country
    
    Args:
        country_code(string) - country code
        year - year
    
    """
    
    for element in requests.get(f"https://date.nager.at/Api/v1/Get/{countrycode}/{year}").json():
        print(f"{element.get('date')}: {element.get('name')}")

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
    """
    parser = ArgumentParser()
    parser.add_argument("countrycode", help="country code")
    parser.add_argument("year", help="year")
    return parser.parse_args(arglist)

if __name__ == "__main__":

    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    get_holidays(arguments.countrycode, arguments.year)