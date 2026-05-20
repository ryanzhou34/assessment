import tkinter as tk
from tkinter import messagebox

QUESTIONS = [
    {"question": "When did World War II end?", "choices": ["1945", "1946", "1943", "1939"], "answer": "1945"},
    {"question": "When was the Treaty of Waitangi signed?", "choices": ["1840", "1841", "1839", "1842"], "answer": "1840"},
    {"question": "Did Hitler serve in World War I?", "choices": ["Yes", "No"], "answer": "Yes"},
    {"question": "Did Napoleon die in exile on Elba?", "choices": ["Yes", "No"], "answer": "No"},
    {"question": "When did World War I start?", "choices": ["1914", "1918", "1939", "1920"], "answer": "1914"},
    {"question": "When did the Cold War end?", "choices": ["1991", "1989", "1945", "1979"], "answer": "1991"},
    {"question": "When was communist China created?", "choices": ["1949", "1950", "1962", "1972"], "answer": "1949"},
    {"question": "When was the Sino-Indian War?", "choices": ["1962", "1979", "1950", "1991"], "answer": "1962"},
    {"question": "When was the Sino-Vietnamese War?", "choices": ["1979", "1962", "1949", "1989"], "answer": "1979"},
    {"question": "When did Nixon visit China?", "choices": ["1972", "1971", "1979", "1969"], "answer": "1972"}
]

root = tk.Tk()
root.title("History Quiz")
root.geometry("400x300")

question_number = 0

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, width=40)
question_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

def check_answer(selected_choice):
    global question_number

    current_question = QUESTIONS[question_number]
    if selected_choice == current_question["answer"]:
        messagebox.showinfo("Correct!", "That's the correct answer!")
    else:
        messagebox.showerror("Incorrect", f"Wrong answer! The correct answer was: {current_question['answer']}")

    question_number += 1
    if question_number < len(QUESTIONS):
        show_question()
    else:
        question_label.config(text="Quiz Completed!")
        for widget in button_frame.winfo_children():
            widget.destroy()

def show_question():
    global question_number

    for widget in button_frame.winfo_children():
        widget.destroy()

    current_question = QUESTIONS[question_number]
    question_label.config(text=current_question["question"])

    for choice in current_question["choices"]:
        tk.Button(
            button_frame,
            text=choice,
            width=20,
            command=lambda c=choice: check_answer(c)
        ).pack(pady=5)

show_question()
root.mainloop()