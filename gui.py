import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
root.geometry("500x550")
root.config(bg="#2C3E50")

question_number = 0
score = 0

title_label = tk.Label(
    root,
    text="History Quiz",
    font=("Arial", 24, "bold"),
    bg="#2C3E50",
    fg="white"
)
title_label.pack(pady=10)
try:
    image = Image.open("history.jpg") 
    image = image.resize((250, 150))
    quiz_image = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=quiz_image, bg="#2C3E50")
    image_label.pack(pady=10)

except:
    image_label = tk.Label(
        root,
        text="Image not found",
        font=("Arial", 12),
        bg="#2C3E50",
        fg="white"
    )
    image_label.pack(pady=10)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    wraplength=420,
    bg="#34495E",
    fg="white",
    padx=15,
    pady=15
)
question_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack()

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 12, "bold"),
    bg="#2C3E50",
    fg="white"
)
score_label.pack(pady=15)


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
            width=25,
            font=("Arial", 12),
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            command=lambda c=choice: check_answer(c)
        ).pack(pady=5)


def check_answer(selected_choice):
    global question_number, score

    current_question = QUESTIONS[question_number]

    if selected_choice == current_question["answer"]:
        score += 1
        score_label.config(text=f"Score: {score}")
        messagebox.showinfo("Correct!", "That's the correct answer!")
    else:
        messagebox.showerror(
            "Incorrect",
            f"Wrong answer! The correct answer was: {current_question['answer']}"
        )

    question_number += 1

    if question_number < len(QUESTIONS):
        show_question()
    else:
        question_label.config(
            text=f"Quiz Completed! Your final score is {score}/{len(QUESTIONS)}"
        )

        for widget in button_frame.winfo_children():
            widget.destroy()


show_question()
root.mainloop()