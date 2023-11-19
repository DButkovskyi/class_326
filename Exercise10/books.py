"""A template for a python script deliverable for INST326.

Driver: Danyil Butkovskyi
Navigator: None
Assignment: Exercise 10, books
Date: 11_15_23

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sqlite3
import csv

class BooksDatabase:
    """
    A class to handle the database operations for the books data.
    """

    def __init__(self, db_filename):
        """
        Initializes the database connection.
        """
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                publication_year TEXT
            )
        """)


    def input_data(self, csv_filename):
        """
        Loads the data from CSV file into the database.
        """
        with open(csv_filename, 'r', encoding='utf-8') as file:
            file = csv.reader(file)
            current_id = 0
            for record in file:
                # Check if the first column is a digit, if so use it as the ID
                if record and record[0].strip().isdigit():
                    current_id = int(record[0].strip())
                else:
                    current_id += 1  # Increment the ID for next row without ID
                
                title = record[1].strip()
                author = record[2].strip()
                year = record[3].strip()
                
                self.cursor.execute("""
                    INSERT OR IGNORE INTO books (id, title, author, publication_year)
                    VALUES (?, ?, ?, ?)
                """, (current_id, title, author, year))

            self.connection.commit()

if __name__ == "__main__":
    db = BooksDatabase('books.db')
    db.input_data('books.csv')
    db.connection.close()