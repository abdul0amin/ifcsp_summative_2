#Handles loading quiz questions from a CSV file.
#This function is impure since it depends on external file data.


import csv


def load_questions(filename):
    #Load quiz questions from a CSV file.; Args: filename (str): Path to the question bank CSV file.; Returns: list: A list of dictionaries representing quiz questions.
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
