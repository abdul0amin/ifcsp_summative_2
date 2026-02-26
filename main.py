
#GUI entry point for the Integrated Risk Management (IRM) quiz.
# Collects and validates user names
# Show previous quiz attempts
# Run a multiple-choice quiz
# Score and save results persistently
# Ensure the user selects an option before proceeding

import tkinter as tk
from tkinter import messagebox
from questions_loader import load_questions
from quiz_logic import (
    clean_name,
    is_name_not_empty,
    is_valid_length,
    contains_only_letters,
    select_random_questions,
    check_answer,
)
from records_manager import save_score
import csv
from datetime import datetime

QUIZ_FILE = "question_bank.csv"
RECORDS_FILE = "quiz_records.csv"


class IRMQuizApp:
    #Class to handle the IRM quiz GUI, flow, and scoring.

    def __init__(self, master):

        #Initialize the GUI and quiz state.; Args: master (tk.Tk): The root Tkinter window.
        self.master = master
        self.master.title("IRM Quiz")
        self.master.geometry("700x500")  # larger window for readability
        self.master.resizable(False, False)

        self.name = ""
        self.questions = load_questions(QUIZ_FILE)
        self.quiz_questions = []
        self.current_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        self.build_name_input_screen()

    def build_name_input_screen(self):
        #Display the initial name input screen.
        self.clear_window()

        tk.Label(self.master, text="Enter your name:", font=("Arial", 14)).pack(pady=20)
        self.name_entry = tk.Entry(self.master, font=("Arial", 14))
        self.name_entry.pack(pady=10)
        tk.Button(self.master, text="Start Quiz", font=("Arial", 14), command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        #Validate the name and start the quiz.; Shows previous scores if available.
        name = self.name_entry.get()

        if not (is_name_not_empty(name) and is_valid_length(name) and contains_only_letters(name)):
            messagebox.showerror(
                "Invalid Name", 
                "Name must be 2–50 characters long and contain only letters."
            )
            return

        self.name = clean_name(name)
        self.show_previous_scores()
        self.quiz_questions = select_random_questions(self.questions, 10)
        self.current_index = 0
        self.score = 0
        self.show_question()

    def show_previous_scores(self):
        #Display the user's previous scores in a pop-up if any exist.
        try:
            with open(RECORDS_FILE, newline="") as f:
                reader = csv.reader(f)
                records = [row for row in reader if row[0] == self.name]
                if records:
                    scores_text = "Your previous quiz scores:\n"
                    for row in records:
                        timestamp = datetime.fromisoformat(row[2]).strftime("%Y-%m-%d %H:%M")
                        scores_text += f"{row[1]}/10 on {timestamp}\n"
                    messagebox.showinfo("Previous Scores", scores_text)
        except FileNotFoundError:
            # No records yet
            pass

    def show_question(self):
        #Display the current question and multiple-choice options.
        self.clear_window()

        if self.current_index >= len(self.quiz_questions):
            # Quiz completed
            messagebox.showinfo(
                "Quiz Completed",
                f"{self.name}, your score: {self.score}/{len(self.quiz_questions)}\n"
                "Your score has been saved."
            )
            save_score(self.name, self.score, RECORDS_FILE)
            self.master.quit()
            return

        # Get the current question
        question = self.quiz_questions[self.current_index]

        tk.Label(
            self.master, 
            text=f"Question {self.current_index + 1}: {question['question']}",
            font=("Arial", 14),
            wraplength=650,
            justify="left"
        ).pack(pady=20)

        self.selected_answer.set("")  # Reset selection for this question

        # Create radio buttons for options
        options = ["option_a", "option_b", "option_c", "option_d"]
        for idx, opt in enumerate(options, start=1):
            tk.Radiobutton(
                self.master,
                text=question[opt],
                variable=self.selected_answer,
                value=str(idx),
                font=("Arial", 12),
                wraplength=650,
                anchor="w",
                justify="left"
            ).pack(fill="x", padx=50, pady=5)

        tk.Button(
            self.master,
            text="Next",
            font=("Arial", 14),
            command=self.next_question
        ).pack(pady=20)

    def next_question(self):
        #Validate that the user selected an option before moving on.; Update score if correct, then show next question.
        if not self.selected_answer.get():
            messagebox.showerror("No Selection", "Please select an option before continuing.")
            return

        question = self.quiz_questions[self.current_index]

        if check_answer(self.selected_answer.get(), question["correct"]):
            self.score += 1

        self.current_index += 1
        self.show_question()

    def clear_window(self):
        #Remove all widgets from the window.
        for widget in self.master.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = IRMQuizApp(root)
    root.mainloop()
