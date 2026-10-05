import tkinter as tk
import random

# Суроолор
questions = [
    {
        "question": "Кыргызстандын борбору кайсы шаар?",
        "answers": ["Ош", "Бишкек", "Талас", "Нарын"],
        "correct": "Бишкек"
    },
    {
        "question": "Python деген эмне?",
        "answers": ["Оюн", "Программалоо тили", "Телефон", "Компьютер"],
        "correct": "Программалоо тили"
    },
    {
        "question": "5 + 5 = ?",
        "answers": ["8", "10", "15", "20"],
        "correct": "10"
    },
    {
        "question": "Жердин спутниги эмне?",
        "answers": ["Күн", "Марс", "Ай", "Венера"],
        "correct": "Ай"
    },
    {
        "question": "1 километрде канча метр бар?",
        "answers": ["10", "100", "1000", "500"],
        "correct": "1000"
    },
    {
        "question": "Python'до экранга текст чыгаруу үчүн эмне колдонулат?",
        "answers": ["print()", "input()", "write()", "text()"],
        "correct": "print()"
    }
]

# Суроолорду аралаштыруу
random.shuffle(questions)

current_question = 0
score = 0


# Жаңы суроону көрсөтүү
def show_question():
    global current_question

    if current_question >= len(questions):
        finish_game()
        return

    q = questions[current_question]

    question_label.config(
        text=f"Суроо {current_question + 1}/{len(questions)}\n\n{q['question']}"
    )

    for i in range(4):
        answer_buttons[i].config(
            text=q["answers"][i],
            state="normal"
        )


# Жоопту текшерүү
def check_answer(answer):
    global current_question, score

    correct_answer = questions[current_question]["correct"]

    if answer == correct_answer:
        score += 1
        result_label.config(text="✅ Туура жооп!", fg="green")
    else:
        result_label.config(
            text=f"❌ Туура эмес!\nТуура жооп: {correct_answer}",
            fg="red"
        )

    current_question += 1

    # Бир аз күтүп кийинки суроого өтүү
    root.after(1000, next_question)


# Кийинки суроо
def next_question():
    result_label.config(text="")
    show_question()


# Оюн бүттү
def finish_game():
    question_label.config(
        text=f"🎉 Оюн бүттү!\n\nСенин упайың: {score}/{len(questions)}"
    )

    for button in answer_buttons:
        button.config(state="disabled")

    restart_button.pack(pady=15)


# Кайра баштоо
def restart_game():
    global current_question, score

    current_question = 0
    score = 0

    random.shuffle(questions)

    restart_button.pack_forget()

    show_question()


# Терезе
root = tk.Tk()
root.title("❓ Суроо - Жооп оюну")
root.geometry("500x600")
root.resizable(False, False)

# Башкы аталыш
title_label = tk.Label(
    root,
    text="🧠 Суроо - Жооп",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)

# Суроо
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold"),
    wraplength=450,
    justify="center"
)
question_label.pack(pady=20)

# Жооп баскычтары
answer_buttons = []

for i in range(4):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 16),
        width=30,
        height=2,
        command=lambda i=i: check_answer(
            questions[current_question]["answers"][i]
        )
    )

    button.pack(pady=5)

    answer_buttons.append(button)


# Натыйжа
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=15)

# Кайра баштоо
restart_button = tk.Button(
    root,
    text="🔄 Кайра баштоо",
    font=("Arial", 16, "bold"),
    command=restart_game
)

# Оюнду баштоо
show_question()

root.mainloop()