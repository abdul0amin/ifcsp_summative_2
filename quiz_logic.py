#Core quiz logic and validation functions.
#Pure functions are used where possible to make testing easier.

import random

def clean_name(name: str) -> str:
    #Trim whitespace and convert to title case.
    return name.strip().title()

def is_name_not_empty(name: str) -> bool:
    #Check that the name is not empty.
    return name.strip() != ""

def is_valid_length(name: str) -> bool:
    #Ensure the name length is between 2 and 50 characters.
    return 2 <= len(name.strip()) <= 50

def contains_only_letters(name: str) -> bool:
    #Ensure name contains only alphabetic characters and spaces.
    return name.replace(" ", "").isalpha()

def select_random_questions(questions: list, amount: int = 10) -> list:
    #Randomly select questions from a list.
    return random.sample(questions, min(amount, len(questions)))

def check_answer(user_answer, correct_answer) -> bool:
    #Compare the user's answer with the correct one.
    return str(user_answer) == str(correct_answer)
