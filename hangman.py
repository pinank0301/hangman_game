import tkinter as tk
import random
import threading

# List of words for the game
words = ['python', 'hangman', 'programming', 'developer', 'computer', 'algorithm', 'machine', 'software', 'hardware', 'artificial']

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# Function to check if the player has guessed the word
def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function to update the game state
def update_game():
    guess = entry.get().lower()
    if guess and guess not in guessed_letters:
        guessed_letters.append(guess)
        if guess not in word:
            attempts_left.set(attempts_left.get() - 1)
            result_label.config(text="Wrong guess!")
        else:
            result_label.config(text="Good guess!")
        
        # Check if player has won
        if check_win(word, guessed_letters):
            result_label.config(text=f"Congratulations! You've guessed the word: {word}")
            restart_button.pack()
        
        # Check if game over
        if attempts_left.get() == 0:
            result_label.config(text=f"Game Over! The word was: {word}")
            restart_button.pack()
        
        # Update display
        word_display.set(display_word(word, guessed_letters))
        guessed_letters_label.config(text=f"Guessed letters: {', '.join(guessed_letters)}")
    
    entry.delete(0, tk.END)

# Function to restart the game
def restart_game():
    global word, guessed_letters
    word = random.choice(words)
    guessed_letters = []
    attempts_left.set(6)
    word_display.set(display_word(word, guessed_letters))
    guessed_letters_label.config(text="Guessed letters: ")
    result_label.config(text="")
    restart_button.pack_forget()
    start_timer()  # Restart the timer

# Function to start the timer (2 minutes countdown)
def start_timer():
    global remaining_time
    remaining_time = 120  # 2 minutes in seconds
    update_timer()

# Function to update the timer
def update_timer():
    global remaining_time
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    timer_label.config(text=f"Time left: {minutes:02}:{seconds:02}")
    
    # If the time is up, end the game
    if remaining_time <= 0:
        result_label.config(text="Time's up! Game Over!")
        restart_button.pack()
    else:
        # Decrease the remaining time by 1 second and update every 1000 ms (1 second)
        remaining_time -= 1
        root.after(1000, update_timer)  # Schedule the function to run every second

# Initialize the Tkinter root window
root = tk.Tk()

# Initialize game variables after creating the root window
attempts_left = tk.IntVar(value=6)

# Initialize game variables
word = random.choice(words)
guessed_letters = []

# Set up the GUI
word_display = tk.StringVar()
word_display.set(display_word(word, guessed_letters))

# Game UI
root.title("Hangman Game")

title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 20))
title_label.pack()

word_label = tk.Label(root, textvariable=word_display, font=("Helvetica", 16))
word_label.pack()

guessed_letters_label = tk.Label(root, text="Guessed letters: ", font=("Helvetica", 12))
guessed_letters_label.pack()

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack()

guess_button = tk.Button(root, text="Guess", font=("Helvetica", 14), command=update_game)
guess_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

attempts_label = tk.Label(root, textvariable=attempts_left, font=("Helvetica", 14))
attempts_label.pack()

timer_label = tk.Label(root, text="Time left: 02:00", font=("Helvetica", 14))
timer_label.pack()

restart_button = tk.Button(root, text="Restart Game", font=("Helvetica", 14), command=restart_game)

# Start the game and timer
start_timer()

# Start the main loop
root.mainloop()
