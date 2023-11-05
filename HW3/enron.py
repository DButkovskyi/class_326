import re
import argparse
import sys

class Email:
    """Class to store individual email messages."""
    def __init__(self, message_id, date, subject, sender, receiver, body):
        """
        Initializes an Email object.

        Args:
            message_id (str): The unique message identifier.
            date (str): The date associated with the email.
            subject (str): The subject line of the email.
            sender (str): The sender's email address.
            receiver (str): The receiver's email address.
            body (str): The content of the email.
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body
    
    def __repr__(self):
        """
        Returns a formatted representation of the Email object.
        """
        return (f"ID\n{self.message_id}\n\nDATE\n{self.date}\n\nSUBJECT\n{self.subject}\n\nSENDER\n{self.sender}\n\nRECEIVER\n{self.receiver}\n\nBODY\n{self.body}")

class Server:
    """Class to store all emails found in the dataset."""
    def __init__(self, path):
        """
        Initializes a Server object, reads the emails from a file, and extracts necessary data.

        Args:
            path (str): The path to the text file containing emails.
        """
        self.emails = []
        with open(path, 'r') as file:
            data = file.read()
            emails_data = data.split("End Email\"")  # Split by "End Email"
            for email_data in emails_data:

                # Using regex to extract required email components
                message_id = re.search(r"Message-ID: <(.*?)>", email_data)
                date = re.search(r"Date: (.*?)\n", email_data)
                subject = re.search(r"Subject: (.*?)\n", email_data)
                sender = re.search(r"From: (.*?)\n", email_data)
                receiver = re.search(r"To: (.*?)\n", email_data)

                if all((message_id, date, subject, sender, receiver)):

                    # Extracts everything from new line after "X-FileName:" to the start of next "End Email"
                    body_match = re.search(r"X-FileName:.*?\n(.*)\nEnd Email", email_data, re.DOTALL)
                    
                    if body_match:
                        body = body_match.group(1).strip()
                    else:  # If there is no next "End Email"
                        body = re.search(r"X-FileName:.*?\n(.*)", email_data, re.DOTALL).group(1).strip()

                    email = Email(
                        message_id.group(1).strip(),
                        date.group(1).strip(),
                        subject.group(1).strip(),
                        sender.group(1).strip(),
                        receiver.group(1).strip(),
                        body
                    )
                    self.emails.append(email)
                        
def main(path):
    """
    Parses the emails from the file and returns the count of processed emails.

    Args:
        path (str): The path to the text file containing emails.

    Returns:
        int: The count of processed emails.
    """
    server = Server(path)
    return len(server.emails)

def parse_args(args_list):
    """
    Parses command-line arguments.

    Args:
        args_list (list): A list of strings containing command-line arguments.

    Returns:
        ArgumentParser: The ArgumentParser object.
    """
    parser = argparse.ArgumentParser(description='Enron Email Parser')
    parser.add_argument('path', type=str, help='Path to the text file')
    return parser.parse_args(args_list)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    count = main(args.path)
    print(f"Total emails processed: {count}")


