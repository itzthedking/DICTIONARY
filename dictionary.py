import tkinter as tk
from tkinter import messagebox

# A sample Spanish dictionary
spanish_dict = {
    "hola": "hello",
    "amor": "love",
    "mundo": "world",
    "casa": "house",
    "perro": "dog",
    "gato": "cat",
    "feliz": "happy",
    "triste": "sad",
    "gracias": "thank you",
    "libro": "book",
    "agua": "water",
    "sol": "sun"
}

# Function to search for the word in the dictionary
def search_word():
    word = entry.get().strip().lower()
    if word in spanish_dict:
        meaning_label.config(text=f"Meaning: {spanish_dict[word]}")
    else:
        messagebox.showinfo("Not Found", f"The word '{word}' is not in the dictionary.")

# Set up the main window
root = tk.Tk()
root.title("Spanish Dictionary")

# Add a label
label = tk.Label(root, text="Enter a Spanish word to search:", font=("Arial", 14))
label.pack(pady=10)

# Add the search entry box
entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.pack(pady=10)

# Add a search button
search_button = tk.Button(root, text="Search", font=("Arial", 14), command=search_word)
search_button.pack(pady=10)

# Add a label for showing the meaning
meaning_label = tk.Label(root, text="Meaning: ", font=("Arial", 14))
meaning_label.pack(pady=10)

# Run the application
root.mainloop()
