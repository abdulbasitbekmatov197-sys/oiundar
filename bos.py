import tkinter as tk
from tkinter import messagebox

# Негизги терезе
root = tk.Tk()
root.title("менин биринчи оюнум")
root.geometry("700x900")
root.resizable(False, False)

# Кезек
current_player = "X"

# Оюндун талаасы
board = [""] * 9

# Жеңиш комбинациялары
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# Оюнду текшерүү
def check_winner():
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    if "" not in board:
        return "Тең"

    return None


# Баскыч басылганда
def button_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(text=current_player)

    winner = check_winner()

    if winner:
        if winner == "Тең":
            messagebox.showinfo("Оюн бүттү", "Тең чыкты!")
        else:
            messagebox.showinfo("Оюн бүттү", f"{winner} жеңди!")

        reset_game()
        return

    # Кезекти өзгөртүү
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    label.config(text=f"Кезек: {current_player}")


# Оюнду кайра баштоо
def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="")

    label.config(text="Кезек: X")


# Аталышы
title = tk.Label(
    root,
    text="❌ X - O ⭕",
    font=("Arial", 30, "bold")
)
title.pack(pady=15)

# Кезек көрсөтүү
label = tk.Label(
    root,
    text="Кезек: X",
    font=("Arial", 20)
)
label.pack(pady=10)

# Оюн талаасы
game_frame = tk.Frame(root)
game_frame.pack()

buttons = []

for i in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 30, "bold"),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)


# Кайра баштоо баскычы
reset_button = tk.Button(
    root,
    text="🔄 Кайра баштоо",
    font=("Arial", 16, "bold"),
    command=reset_game
)

reset_button.pack(pady=20)


# Программаны иштетүү
root.mainloop()