"""A template for a python script deliverable for INST326.

Driver: Danyil Butkovskyi
Navigator: None
Assignment: Exercise: People
Date: 10_19_23

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import re

def parse_name(text):
    # Use a regular expression to capture the first and last name
    name_pattern = r'(\w+)\s+(\w+)'
    match = re.search(name_pattern, text)
    
    if match:
        first_name = match.group(1)
        last_name = match.group(2)
        return first_name, last_name
    else:
        return None   

def parse_address(text):
    # Use regular expressions to capture street, city, and state
    address_pattern = r'(\d+\s[^\d]+)\s(\w+)\s([A-Z]{2})'
    match = re.search(address_pattern, text)

    if match:
        street = match.group(1)
        city = match.group(2)
        state = match.group(3)
        return Address(street, city, state)
    else:
        return None


def parse_email(text):
    # Use a regular expression to capture the email address
    email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,5})'
    match = re.search(email_pattern, text)
    
    if match:
        email = match.group(1)
        return email
    else:
        return None

class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
    def __repr__(self):
        return f"Address: {self.street}, {self.city}, {self.state}"


class Employee:
    def __init__(self, line):
        # Extract name, address, and email from the line
        first_name, last_name = parse_name(line)
        address = parse_address(line)
        email = parse_email(line)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
    def __repr__(self):
        return f"Employee (First name: {self.first_name}, Last name: {self.last_name}, {self.address}, Email: {self.email})"



def main(input_path):
    employee_list = []
    with open(input_path, 'r') as file:
        for line in file:
            employee = Employee(line)
            employee_list.append(employee)
    
    return employee_list


if __name__ == "__main__":

    input_path = "people.txt"
    employees_text = "\n".join([repr(employee) for employee in main(input_path)])
    with open(f"output_{input_path}", 'w') as file:
        file.write(employees_text)

    print(employees_text)


