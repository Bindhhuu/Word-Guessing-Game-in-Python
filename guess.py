import random
import tkinter as tk

# Initialize the main window
m = tk.Tk()
m.title("Hangman Game")
m.geometry("400x300")
m.configure(bg="black")


# Word bank and game setup
word_bank = ['africa', 'asia', 'australia', 'north america', 'south america', 'antarctica']
word = random.choice(word_bank).lower()
guessed_word = ['_'] * len(word)
attempts = 10

# Display variables
display_word = tk.StringVar()
display_word.set(' '.join(guessed_word))
feedback_text = tk.StringVar()  # For feedback messages
feedback_text.set("Start guessing!")

# Functions for the game logic
def guess_letter(event=None):  # Add event parameter to handle Enter key press
    global attempts
    guess = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)

    # Check input validity
    if len(guess) != 1 or not guess.isalpha():
        feedback_text.set("Please enter a single letter.")
        return

    # Check if guess is correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        display_word.set(' '.join(guessed_word))
        feedback_text.set("Great guess!")
        
        # Check if the word is completely guessed
        if '_' not in guessed_word:
            feedback_text.set(f"Congratulations! The word was '{word}'.")
            guess_button.config(state="disabled")  # Disable further guessing
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts Left: {attempts}")
        feedback_text.set("Wrong guess!")
        if attempts == 0:
            feedback_text.set(f"Game Over! The word was '{word}'.")
            guess_button.config(state="disabled")  # Disable further guessing

# GUI Elements
tk.Label(m, text="Guess the word:", bg='black', fg='lavender').pack(pady=10)
tk.Label(m, textvariable=display_word, font=("Arial", 18)).pack(pady=10)

entry_guess = tk.Entry(m, font=("Arial", 14), width=5)
entry_guess.pack(pady=10)

guess_button = tk.Button(m, text="Guess", command=guess_letter, bg='black', fg='lavender')
guess_button.pack(pady=10)

attempts_label = tk.Label(m, text=f"Attempts Left: {attempts}", font=("Arial", 14), bg='black', fg='lavender')
attempts_label.pack(pady=10)

feedback_label = tk.Label(m, textvariable=feedback_text, font=("Arial", 12), bg='black', fg='lavender')
feedback_label.pack(pady=10)

# Bind the Enter key to the guess_letter function
m.bind('<Return>', guess_letter)

# Start the game loop
m.mainloop()
