"""Identify the most popular movie ratings based on data in two CSV files.
Driver: Danyil Butkovskyi
Navigator: None
Assignment: Movies
Date: 11_3_2023
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from argparse import ArgumentParser
import pandas as pd
import sys


# Replace this comment with your implementation of best_movies().
def best_movies(path_to_movies, path_to_ratings):
    """ Finds best movies using two csv files : movies and ratings
    
    Args:
        path_to_movies: string path to csv file with movies
        path_to_ratings: string path to csv file with ratings
    
    Returns:
        average_ratings: Top 5 movies sorted
    """
    movies_df = pd.read_csv(path_to_movies)
    ratings_df = pd.read_csv(path_to_ratings)
    combined_df = pd.merge(movies_df, ratings_df, how="inner", right_on="item id", left_on="movie id")
    average_ratings = combined_df.groupby("movie title")["rating"].mean()
    return average_ratings.sort_values(ascending=False)

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)

best_movies("movies.csv", "ratings.csv")
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())

