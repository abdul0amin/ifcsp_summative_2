#Handles persistent storage and retrieval of quiz results.
#All functions that interact with external CSV files are impure.


import csv
from datetime import datetime


def save_score(name, score, filename="quiz_records.csv"):
    #Append a quiz result to a CSV file.; Args: name (str): The participant's name. score (int): The score obtained in the quiz. filename (str): CSV file where scores are stored.; Returns: None
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score, datetime.now()])


def load_scores_for_user(name, filename="quiz_records.csv"):
    #Load all previous quiz scores for a given user.; Args: name (str): The participant's name. filename (str): CSV file where scores are stored.; Returns: list of tuples: Each tuple contains (timestamp_str, score)
    scores = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue  # Skip invalid rows
                row_name, row_score, row_time = row
                if row_name.strip().lower() == name.strip().lower():
                    scores.append((row_time, int(row_score)))
    except FileNotFoundError:
        # File doesn't exist yet; no scores
        pass

    return scores
