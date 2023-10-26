from argparse import ArgumentParser
import sys
# Replace this comment with your implementation of get_winner().
def to_dict(filename, value_type=str):
  """ Read a two-column, tab-delimited file and return the lines as
  a dictionary with data from the first column as keys and data from
  the second column as values.
  Args:
  filename (str): the file to be read.
  value_type (data type): the type of the values in the second
  column (default: str).
  Raises:
  ValueError: encountered a line with the wrong number of columns.
  Returns:
  dict: the data from the file.
  """
  lines = dict()
  with open(filename, "r", encoding="utf-8") as f:
    for n, line in enumerate(f, start=1):
      line = line.strip()
      if not line:
        continue
      values = line.split("\t")
      if len(values) != 2:
        raise ValueError("unexpected number of columns on line" 
                         f" {n} of {filename}")
      lines[values[0]] = value_type(values[1])
  return lines


def read_data(elector_file, outcome_file):
  """ Read elector data and outcome data and return as dictionaries.
  Args:
  elector_file (str): path to the file of electors by state.
  outcome_file (str): path to the file of hypothetical outcomes by
  state.
  Returns:
  tuple of dict, dict: the elector data and outcome data. Keys in
  each dictionary will be state names.
  """
  elector_dict = to_dict(elector_file, value_type=int)
  outcome_dict = to_dict(outcome_file)
  return elector_dict, outcome_dict


def parse_args(arglist):
  """ Parse command-line arguments.
  Args:
  arglist (list of str): list of arguments from the command line.
  Returns:
  namespace: the parsed arguments, as returned by
  argparse.ArgumentParser.parse_args().
  """
  parser = ArgumentParser()
  parser.add_argument("elector_file", help="file of electors by state")
  parser.add_argument("outcome_file", help="file of outcomes by state")
  return parser.parse_args(arglist)

def get_winner(elector_dict, outcome_dict):
  """
    Calculate the winning candidate and total electoral votes.

    This function takes two dictionaries as input: one representing the number of electors
    in each state and the other representing the hypothetical election outcomes in each state.

    Parameters:
    - electors (dict): A dictionary with state names as keys and the number of electors in each state as values.
    - outcomes (dict): A dictionary with state names as keys and the hypothetical election outcomes ("R" for Republican,
                      "D" for Democrat) as values.

    Returns:
    A tuple consisting of:
    - The winning candidate ("R" for Republican, "D" for Democrat, or "Tie" in case of a tie).
    - The total number of electoral votes received by the winning candidate.
  """
  r_votes = 0
  d_votes = 0
  for state, outcome in outcome_dict.items():
    if outcome == "R":
      r_votes += elector_dict.get(state, 0)
    elif outcome == "D":
      d_votes += elector_dict.get(state, 0)
  
  if r_votes > d_votes:
    return ("R", r_votes)
  elif d_votes > r_votes:
    return ("D", d_votes)
  else:
    return ("Tie", d_votes)

if __name__ == "__main__":
  args = parse_args(sys.argv[1:])
  elector_dict, outcome_dict = read_data(args.elector_file, args.outcome_file)
  candidate, votes = get_winner(elector_dict, outcome_dict)
  print(f"{candidate} would win with {votes} electoral votes.")

