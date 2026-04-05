import tkinter as tk
import random

# Word list with hints
word_data = {
    "apple": "A fruit",
    "tiger": "A wild animal",
    "chair": "Used for sitting",
    "robot": "A machine",
    "pizza": "A popular fast food"
}

word = random.choice(list(word_data.keys()))
hint = word_data[word]

display_word = ["_"] * len(word)
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

# Create window
root = tk.Tk()
root.title("Hangman Game 🎮")
root.geometry("500x600")
root.configure(bg="#F7F7F7")

# Functions
def update_display():
    word_label.config(text=" ".join(display_word))
    attempts_label.config(text=f"Attempts left: {max_attempts - wrong_attempts}")

def check_game():
    if "_" not in display_word:
        result_label.config(text="🎉 You Win!", fg="green")
        disable_buttons()
    elif wrong_attempts >= max_attempts:
        result_label.config(text=f"💀 You Lose! Word: {word}", fg="red")
        disable_buttons()

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def on_click(letter):
    global wrong_attempts

    if letter in guessed_letters:
        return

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display_word[i] = letter
        result_label.config(text="✅ Correct!", fg="green")
    else:
        wrong_attempts += 1
        result_label.config(text="❌ Wrong!", fg="red")

    update_display()
    check_game()

def show_hint():
    hint_label.config(text=f"Hint: {hint}")

# UI
title = tk.Label(root, text="Hangman Game", font=("Arial", 22, "bold"), bg="#F7F7F7")
title.pack(pady=10)

word_label = tk.Label(root, text=" ".join(display_word), font=("Arial", 24), bg="#F7F7F7")
word_label.pack(pady=20)

attempts_label = tk.Label(root, text="", font=("Arial", 14), bg="#F7F7F7")
attempts_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#F7F7F7")
result_label.pack(pady=10)

hint_button = tk.Button(root, text="Show Hint 🧠", command=show_hint, bg="#FFD166")
hint_button.pack(pady=10)

hint_label = tk.Label(root, text="", font=("Arial", 12), bg="#F7F7F7")
hint_label.pack()

# Keyboard Buttons
frame = tk.Frame(root, bg="#F7F7F7")
frame.pack(pady=20)

buttons = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i, letter in enumerate(alphabet):
    btn = tk.Button(frame, text=letter.upper(), width=4, height=2,
                    command=lambda l=letter: on_click(l),
                    bg="#FF6B6B", fg="white")
    btn.grid(row=i//7, column=i%7, padx=5, pady=5)
    buttons.append(btn)

update_display()

root.mainloop()
